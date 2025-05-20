#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

## built in modules
import sys
import os
import io
import logging

## third party modules
import ruamel.yaml
import requests
import requests_cache

class Config:

    project = CAMARA
    view = 'members'
    slug = camarafund
    landscapeMembersCategory = 'Members'
    landscapeMembersSubcategories = [
        {"name": "Premier Membership", "category": "Premier"},
        {"name": "General Membership", "category": "General"},
        {"name": "Associate Membership", "category": "Associate"},
    ]
    landscapeProjectsLevels = [
        {"name": "Active", "level": "active"},
        {"name": "Incubation", "level": "incubation"},
        {"name": "Sandbox", "level": "sandbox"},
    ]
    landscapeProjectsCategory = 'Projects'
    landscapeProjectsSubcategories = [
       {"name": "All", "category": "All"} 
    ]
    basedir = "."
    landscapefile = 'landscape.yml'
    missingcsvfile = 'missing.csv'
    hostedLogosDir = 'hosted_logos'
    memberSuffix = ''
    memberUsePublicMembershipLogo = False
    projectsAddTechnologySector = False
    projectsAddIndustrySector = False
    projectsAddPMOManagedStatus = False
    projectsAddParentProject = False
    projectsAddCategory = True
    projectsDefaultCrunchbase = 'https://www.crunchbase.com/organization/linux-foundation'
    projectsFilterByParentSlug = True
    projectsAssignSIGs = False
    tacAgendaProjectUrl = None
    artworkRepoUrl = None

    def __init__(self, config_file: io.TextIOWrapper = None, view = None):
        if config_file:
            data_loaded = ruamel.yaml.YAML(typ='safe', pure=True).load(config_file)
            self.view = view if self._isValidViewOption(view) else Config.view
            self.basedir = data_loaded.get('basedir',os.path.dirname(os.path.normpath(config_file.name)))
            self.slug = data_loaded.get('slug',self._lookupSlugFromProject(data_loaded.get('project')))
            self.project = data_loaded.get('project',self._lookupProjectFromSlug(self.slug))
            if not self.slug or not self.project:
                raise ValueError("Invalid project specification in config file")
            self.landscapeProjectsCategory = data_loaded.get('landscapeProjectsCategory',Config.landscapeProjectsCategory)
            self.landscapeProjectsLevels = data_loaded.get('landscapeProjectsLevels',Config.landscapeProjectsLevels)
            self.landscapeProjectsSubcategories = data_loaded.get('landscapeProjectsSubcategories',self._getlandscapeProjectsSubcategoriesFromLevels())
            self.landscapeMembersCategory = data_loaded.get('landscapeMembersCategory',Config.landscapeMembersCategory)
            self.landscapeMembersCategory = data_loaded.get('landscapeMemberCategory',Config.landscapeMembersCategory)
            self.landscapeMembersSubcategories = data_loaded.get('landscapeMembersSubcategories',Config.landscapeMembersSubcategories)
            self.landscapeMembersSubcategories = data_loaded.get('landscapeMemberClasses',Config.landscapeMembersSubcategories)
            self.landscapefile = data_loaded.get('landscapefile',Config.landscapefile)
            self.missingcsvfile = data_loaded.get('missingcsvfile',Config.missingcsvfile)
            self.hostedLogosDir = data_loaded.get('hostedLogosDir',Config.hostedLogosDir)
            self.memberSuffix = data_loaded.get('memberSuffix',Config.memberSuffix)
            self.memberUsePublicMembershipLogo = data_loaded.get('memberUsePublicMembershipLogo',Config.memberUsePublicMembershipLogo)
            self.projectsAddTechnologySector = data_loaded.get('projectsAddTechnologySector',Config.projectsAddTechnologySector)
            self.projectsAddIndustrySector = data_loaded.get('projectsAddIndustrySector',Config.projectsAddIndustrySector)
            self.projectsAddPMOManagedStatus = data_loaded.get('projectsAddPMOManagedStatus',Config.projectsAddPMOManagedStatus)
            self.projectsAddParentProject = data_loaded.get('projectsAddParentProject',Config.projectsAddParentProject)
            self.projectsAddCategory = data_loaded.get('projectsAddCategory',Config.projectsAddCategory)
            self.projectsDefaultCrunchbase = data_loaded.get('projectsDefaultCrunchbase',Config.projectsDefaultCrunchbase)
            self.projectsFilterByParentSlug = data_loaded.get('projectsFilterByParentSlug',Config.projectsFilterByParentSlug)
            self.projectsAssignSIGs = data_loaded.get('projectsAssignSIGs',Config.projectsAssignSIGs)
            self.tacAgendaProjectUrl = data_loaded.get('tacAgendaProjectUrl',Config.tacAgendaProjectUrl)
            self.artworkRepoUrl = data_loaded.get('artworkRepoUrl',Config.artworkRepoUrl)

    def _isValidViewOption(self,view):
        return view in ['projects','members'] 

    @property
    def landscapeCategory(self):
        if self.view == 'projects':
            return self.landscapeProjectsCategory
        elif self.view == 'members':
            return self.landscapeMembersCategory

    @property
    def landscapeSubcategories(self):
        if self.view == 'projects':
            return self.landscapeProjectsSubcategories
        elif self.view == 'members':
            return self.landscapeMembersSubcategories

    def _lookupProjectFromSlug(self, slug):
        singleSlugEndpointURL = 'https://api-gw.platform.linuxfoundation.org/project-service/v1/public/projects?slug={}' 
        session = requests_cache.CachedSession()
        if slug:
            with session.get(singleSlugEndpointURL.format(slug)) as endpointResponse:
                parentProject = endpointResponse.json()
                if len(parentProject.get('Data')) > 0: 
                    return parentProject.get('Data')[0].get("ProjectID")
        
        logging.getLogger().warning("Couldn't find project for slug '{}'".format(slug)) 
        
        return None

    def _lookupSlugFromProject(self,project):
        singleProjectEndpointURL = 'https://api-gw.platform.linuxfoundation.org/project-service/v1/public/projects?$filter=projectId%20eq%20{}'
        session = requests_cache.CachedSession()
        if project:
            with session.get(singleProjectEndpointURL.format(project)) as endpointResponse:
                parentProject = endpointResponse.json()
                if len(parentProject.get('Data')) > 0: 
                    return parentProject.get('Data',[])[0].get("Slug")
        
        logging.getLogger().warning("Couldn't find slug for project '{}'".format(project)) 
        
        return None

    def _getlandscapeProjectsSubcategoriesFromLevels(self):
        for level in self.landscapeProjectsLevels:
            self.landscapeProjectsSubcategories.append({'name':level['name'],'category':level['name']})

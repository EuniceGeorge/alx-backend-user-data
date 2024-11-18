#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""manage API Authentication"""
from flask import request
from typing import List, TypeVar


class Auth(object):
    """manage API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that returns boolean"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        """check if path is excluded"""
        for path in excluded_paths:
            if path.endswith('*') and path.startswith(path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorizedmethod that returns boolean"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None

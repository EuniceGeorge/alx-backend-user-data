#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""manage API"""
from flask import request
from typing import List


class Auth(object):
    """manage API"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that returns boolean"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorizedmethod that returns boolean"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        if request is None:
            return None

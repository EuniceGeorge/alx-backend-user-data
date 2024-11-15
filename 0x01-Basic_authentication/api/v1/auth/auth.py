#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""manage API Authentication"""
from flask import request
from typing import List


class Auth(object):
    """manage API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that returns boolean
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths
        Returns:
            bool: Currently always returns False."""
        return False

    def authorization_header(self, request=None) -> str:
        """authorizedmethod that returns boolean"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None

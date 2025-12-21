#!/usr/bin/env python
"""Launcher script for innovation-socratic MCP server"""
import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Now run the server
import asyncio
from src.server import main

if __name__ == "__main__":
    asyncio.run(main())

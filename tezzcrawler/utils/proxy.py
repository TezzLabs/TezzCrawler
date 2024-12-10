"""Proxy configuration utilities."""

from typing import Optional, Dict


def get_proxy(
    proxy_url: str,
    proxy_port: int,
    proxy_username: str,
    proxy_password: str
) -> Dict[str, str]:
    """Configure proxy settings for HTTP requests.
    
    Args:
        proxy_url: The URL of the proxy server
        proxy_port: The port number of the proxy server
        proxy_username: Username for proxy authentication
        proxy_password: Password for proxy authentication
    
    Returns:
        dict: A dictionary containing proxy configuration
    """
    return {
        "http": f"http://{proxy_username}:{proxy_password}@{proxy_url}:{proxy_port}",
        "https": f"http://{proxy_username}:{proxy_password}@{proxy_url}:{proxy_port}",
    }


def create_proxy_config(
    proxy_url: Optional[str] = None,
    proxy_port: Optional[int] = None,
    proxy_username: Optional[str] = None,
    proxy_password: Optional[str] = None,
) -> Optional[Dict[str, str]]:
    """Create proxy configuration if proxy details are provided.
    
    Args:
        proxy_url: Optional proxy URL
        proxy_port: Optional proxy port
        proxy_username: Optional proxy username
        proxy_password: Optional proxy password
    
    Returns:
        Optional[dict]: Proxy configuration if all details are provided, None otherwise
    """
    if all([proxy_url, proxy_port, proxy_username, proxy_password]):
        return get_proxy(proxy_url, proxy_port, proxy_username, proxy_password)
    return None

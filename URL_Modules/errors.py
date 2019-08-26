class WebsiteNotFound(Exception):
    """
        *WebsiteNotFound raise*
        
        When requests can't reach a website,
        this error should pop up.
        (This should make it more clear)
    """
    pass


class KillSwitch(Exception):
    """
        *KillSwitch raise*

        Once a client sends a KillSwitch (your-ip/closeconnection)
        the handler automatically will raise the KillSwitch Exception.
    """
    pass

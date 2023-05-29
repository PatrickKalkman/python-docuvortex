def getattr_or_default(obj, attr, default=None):
    """Get an attribute from an object, returning a default value if the attribute """
    """is not found or its value is None."""
    value = getattr(obj, attr, default)
    return value if value is not None else default

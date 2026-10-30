# Build: ca531e282f2bbfbef2d0098ee3d5f5f7

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

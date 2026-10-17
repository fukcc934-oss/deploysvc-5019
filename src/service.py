"""Deploy-facing service entry point."""
from vendor.ratelib import RateLimiter

SERVICE_NAME = "deploysvc"
MAX_REQ_PER_SEC = 30
BURST = 90

limiter = RateLimiter(BURST, MAX_REQ_PER_SEC)


def handle(request):
    if not limiter.allow():
        return {"status": 429}
    return {"status": 200, "service": SERVICE_NAME}

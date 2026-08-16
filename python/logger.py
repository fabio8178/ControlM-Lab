import logging
from pathlib import Path

pasta_logs = Path("../logs")
pasta_logs.mkdir(exist_ok=True)

logging.basicConfig(
    filename=pasta_logs / "app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

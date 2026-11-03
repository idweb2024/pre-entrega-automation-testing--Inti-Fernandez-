import logging
import pathlib

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

logger = logging.getLogger('talentolab')
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(audit_dir / 'suite.log', encoding='utf-8')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(name)s – %(message)s',
        datefmt='%H:%M:%S'
    ))
    logger.addHandler(handler)


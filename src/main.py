from .utils.log_utils import get_logger
from .config.config import config


logger = get_logger(config.log_file)


def main(args):
    try:
        if args.test:
            logger.info("Testing...")
        elif args.demo_func:
            logger.info("Demo")
            from .demo.demo_func import demo_func
            x = int(args.input)
            logger.info('x ** 2 = {}'.format(demo_func(x)))
        else:
            logger.error('No this command !!!')
            raise NotImplementedError('No this command !!!')
    except Exception:
        logger.exception('Error:')

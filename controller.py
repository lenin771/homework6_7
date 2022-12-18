import model
import view
import logger


def run():
    mode = view.choose_mode()
    result = model.run_contact(mode)
    view.show_results(result)
    logger.log_result(result)
    

from base64 import b64decode
import json
import logging
import os.path

__all__ = ["validate_traffic_report"]
logging.basicConfig(level=logging.INFO)

def validate_traffic_report(reportFile: str) -> bool:
    """
    Simple function that acts as a tolerance validator for the overall success rate
    ratio of all traffic into the service endpoint
    """

    logging.info("START validating traffic report ...")

    if not os.path.isfile(reportFile):
        # No traffic report to begin with, so this is a no-op validation
        # that will always PASS
        logging.info("No traffic started yet... All OK so far.")
        return True

    # Each line in the transformed report file will have one JSON object representing
    # a single HTTP request made to the service.
    #
    # We validate that there must not be any errors for any requests made.
    with open(reportFile) as f:
        for line in f:
            error = json.loads(line).get("error")
            #error = json.loads(b64decode(json.loads(line).get("error")))
            #error = record.get("error")
            if error:
                logging.error("Found error(s) in the traffic report. This indicates that one/more requests actually failed during the experiment.\nThe service is *NOT* highly available. This experiment will fail.")
                logging.error(error)
                return False

    logging.info("DONE validating traffic report - All OK.")
    return True
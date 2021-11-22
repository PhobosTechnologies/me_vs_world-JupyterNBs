import s3ds_agent as sa


class TrumpAgent(sa.S3DSAgent):

    def __init__(self, starting_vals):

        super().__init__(starting_vals)

    def work(self, req_for_job=10):
        return req_for_job

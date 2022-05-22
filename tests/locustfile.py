from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def show_copetition_list(self):
        with self.client.post(
            "/showSummary", catch_response=True, data={"email": "john@simplylift.co"}
        ) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Request took too long")

    @task
    def pourchase_places_test(self):
        with self.client.post(
            "/purchasePlaces",
            catch_response=True,
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "1",
            },
        ) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure("Request took too long")

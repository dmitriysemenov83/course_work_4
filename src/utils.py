from abc import ABC, abstractmethod
import requests
import json


class GeneralAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(GeneralAPI):

    def get_vacancies(self):
        # Retrieve job vacancies from the HeadHunter API
        pass


class SuperJobAPI(GeneralAPI):

    def get_vacancies(self):
        # Retrieve job vacancies from the SuperJob API
        pass


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary
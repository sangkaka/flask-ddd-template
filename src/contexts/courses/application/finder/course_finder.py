from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound


class CourseFinder:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self, title: str):
        course = self.repository.find_one(title.lower().strip())
        if course:
            raise CourseNotFound()
        return course

from abc import ABC, abstractmethod


class UniversityMember(ABC):
	@abstractmethod
	def perform_duty(self):
		pass


class Student(UniversityMember):
	def perform_duty(self):
		print("Student attends classes and studies.")


class Lecturer(UniversityMember):
	def perform_duty(self):
		print("Lecturer teaches students.")


class Administrator(UniversityMember):
	def perform_duty(self):
		print("Administrator manages university operations.")


members = [Student(), Lecturer(), Administrator()]

for member in members:
	member.perform_duty()

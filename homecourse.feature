Feature: test eduK's home course

        As a user
        I want to load up working videos
        So that I can learn :)

	Scenario:
		Given a user enters eduK
		When we log in
		Then we click submit

	Scenario Outline: course check
		When we click on the "<specific content>"
		Then we should see "<subcontent>"

		Examples:
			|specific content |subcontent |
			|gastronomia page |courses    |
			|random course    |lessons    |
			|random lesson    |a video    |

	Scenario: test search function
		Given we make a search
		Then we should see "courses"
		When we click on the "random course"
		Then we should see "lessons"
		When we click on the "random lesson"
		Then we should see "a video"

	Scenario: favourite course viewing
		When we click on the "gastronomia page"
		Then we should see "courses"
		When we favourite a course
		Then we go to meus cursos
		When we click on the "random course"
		Then we should see "lessons"
		When we click on the "random lesson"
		Then we should see "a video"
		When we click on the "gastronomia page"
		Then we should see "courses"
		When we undo the favourite course

        Scenario: full course check
                Given we make a search
                When we click on the "random course"
		Then we should see "lessons"
                Given we have not completed the course
                When we click on the first lesson
		Then we should see "a video"
                Then we skip to the end of the video
                But go through the assignment if there is no video

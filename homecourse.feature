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

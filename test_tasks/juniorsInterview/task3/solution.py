def appearance(intervals: dict[str, list[int]]) -> int:
    lessonStart, lessonEnd = intervals["lesson"]

    pupilIntervals = []
    tutorIntervals = []

    for i in range(0, len(intervals["pupil"]), 2):
        pupilIntervals.append((intervals["pupil"][i], intervals["pupil"][i + 1]))

    for i in range(0, len(intervals["tutor"]), 2):
        tutorIntervals.append((intervals["tutor"][i], intervals["tutor"][i + 1]))

    presenceIntervals = []

    for pupilStart, pupilEnd in pupilIntervals:
        for tutorStart, tutorEnd in tutorIntervals:
            intersectionStart = max(pupilStart, tutorStart, lessonStart)
            intersectionEnd = min(pupilEnd, tutorEnd, lessonEnd)

            if intersectionStart < intersectionEnd:
                presenceIntervals.append((intersectionStart, intersectionEnd))

    mergedIntervals = []
    for start, end in sorted(presenceIntervals):
        if not mergedIntervals or mergedIntervals[-1][1] < start:
            mergedIntervals.append((start, end))
        else:
            mergedIntervals[-1] = (
                mergedIntervals[-1][0],
                max(mergedIntervals[-1][1], end),
            )

    totalPresenceTime = sum(end - start for start, end in mergedIntervals)

    return totalPresenceTime


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    try:
        for i, test in enumerate(tests):
            testAnswer = appearance(test["intervals"])
            assert (
                testAnswer == test["answer"]
            ), f'Error on test case {i}, got {testAnswer}, expected {test["answer"]}'
        print("Completed tests")
    except Exception as e:
        print(f"Error when tests {e}")

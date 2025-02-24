REVIEW_CHANGES="""
A developer on your team has been working on this task with the following description:
```
{{ development_tasks[current_task_index]['description'] }}
``` 
Based on those instructions, the developer has made changes to file `{{ file_name }}` having the path `{{ file_path }}`.

Here is the original content of this file:
```
{{ old_content }}
```

Here is the diff of the changes:

{% for hunk in hunks %}## Hunk {{ loop.index }}
```diff
{{ hunk }}
```
{% endfor %}

As you can see, there {% if hunks|length == 1 %}is only one hunk in this diff, and it{% else %}are {{hunks|length}} hunks in this diff, and each{% endif %} starts with the `@@` header line.

When reviewing the code changes, apply these principles to decide on each hunk:
- Apply: Approve and integrate the hunk into our core codebase if it accurately delivers the intended functionality or enhancement, aligning with our project objectives. This action confirms the change is beneficial and meets our quality standards.
- Ignore: Use this option sparingly, only when you're certain the entire hunk is incorrect or will introduce errors (logical, syntax, etc.) that could negatively impact the project. Ignoring means the hunk will be completely removed. This should be reserved for cases where the inclusion of the code is definitively more harmful than its absence. Emphasize careful consideration before choosing 'Ignore.' It's crucial for situations where the hunk's removal is the only option to prevent significant issues. Otherwise, 'Rework' might be the better choice to ensure the code's integrity and functionality.
- Rework: Suggest this option if the concept behind the change is valid and necessary but is implemented in a way that introduces problems. This indicates a need for a revision of the hunk to refine its integration without fully discarding the underlying idea.

When deciding what should be done with the hunk you are currently reviewing, pick an option that most reviewers of your skill would choose. Your decisions have to be consistent.

Keep in mind you're just reviewing current file. You don't need to consider if other files are created, dependent packages installed, etc. Focus only on reviewing the changes in this file based on the instructions in the development task description.

Note that the developer may add, modify or delete logging or error handling that's not explicitly asked for, but is a part of good development practice. Unless these logging and error handling additions break something, your decision to apply, ignore or rework the hunk should not be based on this. Base your decision only on functional changes - comments or logging are less important. Importantly, don't ask for a rework just because of logging or error handling changes. Also, take into account this is a junior developer and while the approach they take may not be the best practice, if it's not *wrong*, let it pass. Ask for rework only if the change is clearly bad and would break something.

The developer that wrote this is sometimes sloppy and has could have deleted some parts of the code that contain important functionality and should not be deleted. Pay special attention to that in your review.

-----------------------start-of-output-format---------------------------------------
{
  "hunks": [
    {
      "number": <hunk number 1>,
      "reason": "Reason for applying or ignoring this hunk, or for asking for it to be reworked.",
      "decision": "<Apply or Ignore or Rework>"
    },
    {
      "number": <hunk number 2>,
      "reason": "Reason for applying or ignoring this hunk, or for asking for it to be reworked.",
      "decision": "<Apply or Ignore or Rework>"
    },......
  ],
  "review_notes": "Additional review notes (optional, can be empty)."
}
-----------------------end-of-output-format-----------------------------------------
YOUR OUTPUT:
"""
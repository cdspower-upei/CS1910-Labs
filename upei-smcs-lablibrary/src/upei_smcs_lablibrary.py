# Check if 'np' is already defined in the current namespace
if 'np' not in globals():
    try:
        import numpy as np
    except ImportError:
        np = None

# Check if 'pd' is already defined in the current namespace
if 'pd' not in globals():
    try:
        import pandas as pd
    except ImportError:
        pd = None

# Check if 'plt' is already defined in the current namespace
if 'plt' not in globals():
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        plt = None

# Check if 'widgets' is already defined in the current namespace
if 'widgets' not in globals():
    try:
        import ipywidgets as widgets
    except ImportError:
        widgets = None

# Check if 'ipd' is already defined in the current namespace
if 'ipd' not in globals():
    try:
        import IPython.display as ipd
    except ImportError:
        ipd = None
        
# Lab Form Library - Reusable Components (Widget-Only)
class LabFormLibrary:
    """Reusable form components for interactive lab exercises"""

    @staticmethod
    def create_info_form(title, fields, default_values=None):
        """
        Create a form for collecting student information

        Args:
            title (str): Form title
            fields (list): List of dicts with 'name', 'label', 'placeholder' keys
            default_values (list, optional): List of default values for each field
        """
        field_widgets = {}
        field_containers = []

        for i, field in enumerate(fields):
            # Get placeholder value if provided
            placeholder_value = field.get('placeholder', 'Enter value')
            if default_values and i < len(default_values):
                placeholder_value = str(default_values[i])

            widget = widgets.Text(
                placeholder=placeholder_value,  # ← UPDATED LINE
                description=field['label'],
                style={'description_width': '150px'},
                layout=widgets.Layout(width='400px', margin='0 0 5px 0')
            )
            field_widgets[field['name']] = widget
            field_containers.append(widget)

        submit_button = widgets.Button(
            description='Submit Information',
            button_style='success',
            layout=widgets.Layout(width='200px')
        )

        edit_button = widgets.Button(
            description='Edit Information',
            button_style='warning',
            layout=widgets.Layout(width='200px')
        )

        output_area = widgets.Output()

        def submit_info(button):
            with output_area:
                ipd.clear_output(wait=True)
                print(f"📝 Submitted {title}:")
                print("=" * 40)
                for field in fields:
                    value = field_widgets[field['name']].value
                    print(f"{field['label']}: {value}")
                print("=" * 40)
                print("✅ Information saved! You can edit it anytime using the 'Edit Information' button.")

            form_container.layout.display = 'none'
            submit_button.layout.display = 'none'
            edit_button.layout.display = 'block'

        def edit_info(button):
            form_container.layout.display = 'block'
            submit_button.layout.display = 'block'
            edit_button.layout.display = 'none'

            with output_area:
                ipd.clear_output(wait=True)
                print("📝 Edit mode activated - make your changes and click Submit again.")

        submit_button.on_click(submit_info)
        edit_button.on_click(edit_info)
        edit_button.layout.display = 'none'

        title_widget = widgets.Label(
            value=title,
            layout=widgets.Layout(margin='0 0 15px 0')
        )

        form_container = widgets.VBox([title_widget] + field_containers)
        button_container = widgets.HBox([submit_button, edit_button])
        all_content = widgets.VBox([form_container, button_container, output_area])

        def display_form():
            ipd.display(all_content)

        def get_data():
            return {field['name']: field_widgets[field['name']].value for field in fields}

        return display_form, get_data

    @staticmethod
    def create_question_form(title, questions, answer_key=None, default_values=None):
        """
        Create a question and answer form with proper text wrapping

        Args:
            title (str): Form title
            questions (list): List of dicts with 'number', 'question', 'type' keys
            answer_key (list, optional): List of model answers for reveal
            default_values (list, optional): List of default values for each question
        """
        answer_widgets = []
        question_containers = []

        for i, q in enumerate(questions):
            # Use HTML widget for better text wrapping
            question_html = widgets.HTML(
                value=f"<div style='margin: 15px 0 5px 0; word-wrap: break-word; line-height: 1.4;'><b>Question {q['number']}:</b> {q['question']}</div>",
                layout=widgets.Layout(width='95%', max_width='800px')
            )

            # Get placeholder value if provided
            placeholder_value = 'Enter your answer here...'
            if default_values and i < len(default_values):
                placeholder_value = str(default_values[i])

            if q.get('type', 'text') == 'textarea':
                widget = widgets.Textarea(
                    placeholder=placeholder_value,  # ← UPDATED LINE
                    layout=widgets.Layout(width='95%', height='80px', max_width='800px', margin='0 0 10px 0'),
                    description='',
                    style={'description_width': '0px'}
                )
            else:
                widget = widgets.Text(
                    placeholder=placeholder_value,  # ← UPDATED LINE
                    layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 10px 0'),
                    description='',
                    style={'description_width': '0px'}
                )

            answer_widgets.append(widget)
            question_container = widgets.VBox([question_html, widget],
                layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 10px 0'))
            question_containers.append(question_container)


        submit_button = widgets.Button(
            description='Submit All Answers',
            button_style='success',
            layout=widgets.Layout(width='200px', margin='10px 5px 0 0')
        )

        edit_button = widgets.Button(
            description='Edit Answers',
            button_style='warning',
            layout=widgets.Layout(width='150px', margin='10px 5px 0 0')
        )

        reveal_button = widgets.Button(
            description='Reveal Answers',
            button_style='info',
            layout=widgets.Layout(width='150px', margin='10px 0 0 0')
        )

        output_area = widgets.Output()

        def submit_answers(button):
            with output_area:
                ipd.clear_output(wait=True)
                print(f"📝 Submitted {title}:")
                print("=" * 80)

                for i, (q, widget) in enumerate(zip(questions, answer_widgets)):
                    answer = widget.value.strip() if widget.value.strip() else "(no answer provided)"
                    print(f"\nQuestion {q['number']}:")
                    print(f"Q: {q['question']}")
                    print(f"A: {answer}")
                    print("-" * 60)

                print("\n✅ All answers saved! You can edit them anytime using the 'Edit Answers' button.")

            form_container.layout.display = 'none'
            submit_button.layout.display = 'none'
            edit_button.layout.display = 'block'
            if answer_key:
                reveal_button.layout.display = 'block'

        def edit_answers(button):
            form_container.layout.display = 'block'
            submit_button.layout.display = 'block'
            edit_button.layout.display = 'none'
            reveal_button.layout.display = 'none'

            with output_area:
                ipd.clear_output(wait=True)
                print("📝 Edit mode activated - make your changes and click 'Submit All Answers' again.")

        def reveal_answers(button):
            if not answer_key:
                return

            with output_area:
                ipd.clear_output(wait=True)
                print(f"📚 ANSWER KEY - {title}:")
                print("=" * 100)

                for i, (q, widget) in enumerate(zip(questions, answer_widgets)):
                    student_answer = widget.value.strip() if widget.value.strip() else "(no answer provided)"
                    correct_answer = answer_key[i] if i < len(answer_key) else "No model answer provided"

                    print(f"\nQuestion {q['number']}:")
                    print(f"Q: {q['question']}")
                    print(f"Your Answer: {student_answer}")
                    print(f"Model Answer: {correct_answer}")
                    print("-" * 100)

                print("\n📝 Note: These are model answers. Your responses may vary in wording")
                print("while still demonstrating correct understanding of the concepts.")

        submit_button.on_click(submit_answers)
        edit_button.on_click(edit_answers)
        reveal_button.on_click(reveal_answers)

        edit_button.layout.display = 'none'
        reveal_button.layout.display = 'none'

        title_widget = widgets.Label(value=title, layout=widgets.Layout(margin='0 0 15px 0'))

        form_container = widgets.VBox([title_widget] + question_containers,
            layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 0 0'))

        button_list = [submit_button, edit_button]
        if answer_key:
            button_list.append(reveal_button)

        button_container = widgets.HBox(button_list,
            layout=widgets.Layout(width='95%', max_width='800px', margin='10px 0 0 0'))

        all_content = widgets.VBox([form_container, button_container, output_area],
            layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 0 0'))

        def display_form():
            ipd.display(all_content)

        return display_form

    @staticmethod
    def create_prediction_table(title, code_snippets, expected_answers=None, default_values=None):
        """
        Create a prediction table for code output with fixed vertical output formatting

        Args:
            title (str): Table title
            code_snippets (list): List of code strings to predict
            expected_answers (list, optional): List of expected outputs for reveal
            default_values (list, optional): List of default predictions for each code snippet (used as placeholder text)
        """
        table_widgets = []
        table_rows = []

        title_widget = widgets.Label(value=title, layout=widgets.Layout(margin='0 0 10px 0'))
        instruction_widget = widgets.Label(
            value="Enter your prediction for what each line of Python code will output:",
            layout=widgets.Layout(margin='0 0 15px 0')
        )

        code_header = widgets.Label(
            value="Python Code",
            layout=widgets.Layout(width='50%', margin='0 0 5px 0')
        )
        prediction_header = widgets.Label(
            value="Your Prediction",
            layout=widgets.Layout(width='50%', margin='0 0 5px 0')
        )

        header_row = widgets.HBox([code_header, prediction_header],
            layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 10px 0'))

        for i, code in enumerate(code_snippets):
            code_display = widgets.Label(
                value=code,
                layout=widgets.Layout(width='50%', margin='0 5px 0 0')
            )

            # Get placeholder value if provided
            placeholder_value = 'Enter output or leave blank if none'
            if default_values and i < len(default_values):
                placeholder_value = str(default_values[i])

            prediction_widget = widgets.Text(
                placeholder=placeholder_value,
                layout=widgets.Layout(width='45%', margin='0 0 0 0'),
                description='',
                style={'description_width': '0px'}
            )

            table_widgets.append(prediction_widget)

            row_container = widgets.HBox([code_display, prediction_widget],
                layout=widgets.Layout(width='95%', max_width='800px', margin='2px 0 2px 0'))

            table_rows.append(row_container)

        submit_button = widgets.Button(
            description='Submit Answers',
            button_style='success',
            layout=widgets.Layout(width='150px', margin='10px 5px 0 0')
        )

        edit_button = widgets.Button(
            description='Edit Answers',
            button_style='warning',
            layout=widgets.Layout(width='150px', margin='10px 5px 0 0')
        )

        reveal_button = widgets.Button(
            description='Reveal Answers',
            button_style='info',
            layout=widgets.Layout(width='150px', margin='10px 0 0 0')
        )

        output_area = widgets.Output()

        def submit_answers(button):
            with output_area:
                ipd.clear_output(wait=True)
                print(f"📝 Submitted {title}:")
                print("=" * 80)

                # FIXED: Use vertical format instead of table format
                for i, (code, widget) in enumerate(zip(code_snippets, table_widgets)):
                    answer = widget.value if widget.value else "(no output)"

                    print(f"Code: {code}")
                    print(f"Your Answer: {answer}")
                    print("-" * 40)

                print("✅ Answers saved! You can edit them anytime using the 'Edit Answers' button.")

            table_container.layout.display = 'none'
            submit_button.layout.display = 'none'
            edit_button.layout.display = 'block'
            if expected_answers:
                reveal_button.layout.display = 'block'

        def edit_answers(button):
            table_container.layout.display = 'block'
            submit_button.layout.display = 'block'
            edit_button.layout.display = 'none'
            reveal_button.layout.display = 'none'

            with output_area:
                ipd.clear_output(wait=True)
                print("📝 Edit mode activated - make your changes and click Submit again.")

        def reveal_answers(button):
            if not expected_answers:
                return

            with output_area:
                ipd.clear_output(wait=True)
                print(f"📚 ANSWER KEY - {title} Comparison:")
                print("=" * 80)

                # FIXED: Use vertical format with validation
                for i, (code, widget) in enumerate(zip(code_snippets, table_widgets)):
                    student_answer = widget.value if widget.value else "(no output)"
                    correct_answer = expected_answers[i] if i < len(expected_answers) and expected_answers[i] else "(no output)"

                    print(f"Code: {code}")
                    print(f"Your Answer: {student_answer}")
                    print(f"Correct Answer: {correct_answer}")

                    # Add validation
                    is_correct = student_answer.strip().lower() == correct_answer.strip().lower()
                    result = "✅ Correct" if is_correct else "❌ Incorrect"
                    print(f"Result: {result}")
                    print("-" * 50)

                print("📝 Note: Remember that assignment statements and some expressions don't produce output.")
                print("SyntaxError occurs when Python can't understand the code syntax.")

        submit_button.on_click(submit_answers)
        edit_button.on_click(edit_answers)
        reveal_button.on_click(reveal_answers)

        edit_button.layout.display = 'none'
        reveal_button.layout.display = 'none'

        table_container = widgets.VBox([title_widget, instruction_widget, header_row] + table_rows,
            layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 0 0'))

        button_list = [submit_button, edit_button]
        if expected_answers:
            button_list.append(reveal_button)

        button_container = widgets.HBox(button_list,
            layout=widgets.Layout(width='95%', max_width='800px', margin='10px 0 0 0'))

        all_content = widgets.VBox([table_container, button_container, output_area],
            layout=widgets.Layout(width='95%', max_width='800px', margin='0 0 0 0'))

        def display_form():
            ipd.display(all_content)

        return display_form

    @staticmethod
    def create_validation_form(title, data_rows, headers, correct_answers, instructions="", default_values=None):
        """
        Create a form with validation (correct/incorrect checking)

        Args:
            title (str): Form title
            data_rows (list): List of dicts with fixed data for each row
            headers (list): List of column headers
            correct_answers (list): List of lists with correct answers for validation
            instructions (str): Additional instructions
            default_values (list, optional): List of lists with default values for input columns
        """
        input_widgets = []
        table_rows = []

        title_widget = widgets.Label(value=title, layout=widgets.Layout(margin='0 0 10px 0'))

        instruction_widget = widgets.Label(
            value=instructions,
            layout=widgets.Layout(margin='0 0 15px 0')
        ) if instructions else None

        num_cols = len(headers)
        col_width = f"{90//num_cols}%"

        header_widgets = []
        for header in headers:
            header_label = widgets.Label(
                value=header,
                layout=widgets.Layout(width=col_width, margin='0 0 5px 0')
            )
            header_widgets.append(header_label)

        header_row = widgets.HBox(header_widgets,
            layout=widgets.Layout(width='95%', max_width='600px', margin='5px 0 10px 0'))

        for i, row_data in enumerate(data_rows):
            row_widgets = []
            row_inputs = []
            input_idx = 0

            for j, header in enumerate(headers):
                if header in row_data:
                    widget = widgets.Label(
                        value=str(row_data[header]),
                        layout=widgets.Layout(width=col_width, margin='0 0 2px 0')
                    )
                    row_widgets.append(widget)
                else:
                    # Get placeholder value if provided
                    placeholder_value = 'True/False'
                    if default_values and i < len(default_values) and input_idx < len(default_values[i]):
                        placeholder_value = str(default_values[i][input_idx])

                    input_widget = widgets.Text(
                        placeholder=placeholder_value,  # ← UPDATED LINE
                        layout=widgets.Layout(width=col_width, margin='0 0 2px 0'),
                        description='',
                        style={'description_width': '0px'}
                    )
                    row_widgets.append(input_widget)
                    row_inputs.append(input_widget)
                    input_idx += 1

            input_widgets.append(row_inputs)

            row = widgets.HBox(row_widgets,
                layout=widgets.Layout(width='95%', max_width='600px', margin='2px 0 2px 0'))

            table_rows.append(row)

        submit_button = widgets.Button(
            description='Submit Table',
            button_style='success',
            layout=widgets.Layout(width='150px', margin='10px 5px 0 0')
        )

        edit_button = widgets.Button(
            description='Edit Table',
            button_style='warning',
            layout=widgets.Layout(width='120px', margin='10px 5px 0 0')
        )

        reveal_button = widgets.Button(
            description='Reveal Answers',
            button_style='info',
            layout=widgets.Layout(width='150px', margin='10px 0 0 0')
        )

        output_area = widgets.Output()

        def submit_table(button):
            with output_area:
                ipd.clear_output(wait=True)
                print(f"📝 Submitted {title}:")
                print("=" * 50)

                header_str = " | ".join([f"{h:<8}" for h in headers])
                print(header_str)
                print("-" * 50)

                for i, (row_data, row_inputs) in enumerate(zip(data_rows, input_widgets)):
                    row_values = []
                    input_idx = 0
                    for header in headers:
                        if header in row_data:
                            row_values.append(f"{row_data[header]:<8}")
                        else:
                            answer = row_inputs[input_idx].value.strip() if row_inputs[input_idx].value.strip() else "(blank)"
                            row_values.append(f"{answer:<8}")
                            input_idx += 1

                    print(" | ".join(row_values))

                print("=" * 50)
                print("✅ Table submitted!")

            table_container.layout.display = 'none'
            submit_button.layout.display = 'none'
            edit_button.layout.display = 'block'
            reveal_button.layout.display = 'block'

        def edit_table(button):
            table_container.layout.display = 'block'
            submit_button.layout.display = 'block'
            edit_button.layout.display = 'none'
            reveal_button.layout.display = 'none'

            with output_area:
                ipd.clear_output(wait=True)
                print("📝 Edit mode activated - make your changes and click 'Submit Table' again.")

        def reveal_answers(button):
            with output_area:
                ipd.clear_output(wait=True)
                print(f"📚 ANSWER KEY - {title} Comparison:")
                print("=" * 120)

                comparison_headers = []
                for header in headers:
                    if header not in data_rows[0]:
                        comparison_headers.extend([f"Your {header}", f"Correct {header}"])
                    else:
                        comparison_headers.append(header)
                comparison_headers.append("Result")

                header_str = " | ".join([f"{h:<12}" for h in comparison_headers])
                print(header_str)
                print("-" * 120)

                all_correct = True

                for i, (row_data, row_inputs) in enumerate(zip(data_rows, input_widgets)):
                    row_values = []
                    input_idx = 0
                    row_correct = True

                    for j, header in enumerate(headers):
                        if header in row_data:
                            row_values.append(f"{row_data[header]:<12}")
                        else:
                            student_answer = row_inputs[input_idx].value.strip() if row_inputs[input_idx].value.strip() else "(blank)"
                            correct_answer = correct_answers[i][input_idx] if i < len(correct_answers) and input_idx < len(correct_answers[i]) else "Unknown"

                            is_correct = student_answer.lower() == correct_answer.lower()
                            if not is_correct:
                                row_correct = False
                                all_correct = False

                            row_values.extend([f"{student_answer:<12}", f"{correct_answer:<12}"])
                            input_idx += 1

                    result = "✅ Correct" if row_correct else "❌ Incorrect"
                    row_values.append(f"{result:<12}")

                    print(" | ".join(row_values))

                print("=" * 120)

                if all_correct:
                    print("🎉 Perfect! You got all answers correct!")
                else:
                    print("📝 Review the incorrect answers above and try to understand the logic.")

        submit_button.on_click(submit_table)
        edit_button.on_click(edit_table)
        reveal_button.on_click(reveal_answers)

        edit_button.layout.display = 'none'
        reveal_button.layout.display = 'none'

        container_widgets = [title_widget]
        if instruction_widget:
            container_widgets.append(instruction_widget)
        container_widgets.append(header_row)
        container_widgets.extend(table_rows)

        table_container = widgets.VBox(container_widgets,
            layout=widgets.Layout(width='95%', max_width='700px', margin='0 0 0 0'))

        button_container = widgets.HBox([submit_button, edit_button, reveal_button],
            layout=widgets.Layout(width='95%', max_width='700px', margin='10px 0 0 0'))

        all_content = widgets.VBox([table_container, button_container, output_area],
            layout=widgets.Layout(width='95%', max_width='700px', margin='0 0 0 0'))

        def display_form():
            ipd.display(all_content)

        return display_form

    @staticmethod
    def add_educational_context(title, sections):
        """
        Add educational context section with formatted content

        Args:
            title (str): Main title for the educational section
            sections (list): List of dicts with 'heading' and 'content' keys
        """
        from IPython.display import Markdown, display

        # Build the markdown content
        markdown_content = f"### {title}\n\n"

        for section in sections:
            # Add section heading with emoji if provided
            heading = section['heading']
            if 'emoji' in section:
                heading = f"{section['emoji']} **{heading}**"
            else:
                heading = f"#### **{heading}:**"

            markdown_content += f"{heading}\n"
            markdown_content += f"{section['content']}\n\n"

        # Display the formatted content
        display(Markdown(markdown_content))

    @staticmethod
    def add_quick_context(content):
        """
        Quick way to add educational context with just content

        Args:
            content (str): Markdown-formatted content to display
        """
        from IPython.display import Markdown, display
        display(Markdown(content))
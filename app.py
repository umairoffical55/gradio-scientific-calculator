import gradio as gr
import math


def calculator(num1, num2, operation):
    try:
        if operation == "Addition (+)":
            result = num1 + num2

        elif operation == "Subtraction (-)":
            result = num1 - num2

        elif operation == "Multiplication (*)":
            result = num1 * num2

        elif operation == "Division (/)":
            if num2 == 0:
                return "Error: Division by zero!"
            result = num1 / num2

        elif operation == "Power (x^y)":
            result = num1 ** num2

        elif operation == "Square Root (√x)":
            if num1 < 0:
                return "Error: Cannot take square root of a negative number!"
            result = math.sqrt(num1)

        elif operation == "Log Base 10":
            if num1 <= 0:
                return "Error: Logarithm only defined for positive numbers!"
            result = math.log10(num1)

        elif operation == "Natural Log (ln)":
            if num1 <= 0:
                return "Error: Natural log only defined for positive numbers!"
            result = math.log(num1)

        elif operation == "Sine (sin)":
            result = math.sin(math.radians(num1))

        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(num1))

        elif operation == "Tangent (tan)":
            result = math.tan(math.radians(num1))

        else:
            return "Invalid Operation"

        return f"Result = {result}"

    except Exception as e:
        return f"Error: {str(e)}"


with gr.Blocks(title="Scientific Calculator") as demo:

    gr.Markdown(
        """
        # 🧮 Scientific Calculator
        Perform basic and scientific mathematical operations.
        """
    )

    with gr.Row():
        num1 = gr.Number(label="Number 1", value=0)
        num2 = gr.Number(label="Number 2", value=0)

    operation = gr.Dropdown(
        choices=[
            "Addition (+)",
            "Subtraction (-)",
            "Multiplication (*)",
            "Division (/)",
            "Power (x^y)",
            "Square Root (√x)",
            "Log Base 10",
            "Natural Log (ln)",
            "Sine (sin)",
            "Cosine (cos)",
            "Tangent (tan)"
        ],
        label="Select Operation",
        value="Addition (+)"
    )

    calculate_btn = gr.Button("Calculate", variant="primary")

    result = gr.Textbox(
        label="Result",
        interactive=False
    )

    calculate_btn.click(
        fn=calculator,
        inputs=[num1, num2, operation],
        outputs=result
    )

demo.launch()

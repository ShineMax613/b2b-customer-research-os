"""
Lead Score Calculator

A simple lead qualification tool for B2B exporters and global sales teams.

This tool helps salespeople estimate lead quality before sending a quotation,
catalog, full price list, or follow-up message.

Usage:

Interactive mode:
    python lead_score_calculator.py

Command-line mode:
    python lead_score_calculator.py --company yes --product yes --quantity no --delivery yes --role yes --urgency no --communication yes
"""

import argparse


SCORING_RULES = {
    "company": 15,
    "product": 20,
    "quantity": 20,
    "delivery": 10,
    "role": 15,
    "urgency": 10,
    "communication": 10,
}


QUESTIONS = {
    "company": "Did the customer provide company information?",
    "product": "Did the customer mention a clear product requirement?",
    "quantity": "Did the customer mention quantity?",
    "delivery": "Did the customer mention delivery city or country?",
    "role": "Is the contact role relevant to purchasing or decision-making?",
    "urgency": "Did the customer mention urgency or timeline?",
    "communication": "Is the communication professional and clear?",
}


def normalize_yes_no(value):
    """Convert yes/no input into a boolean value."""

    if value is None:
        return None

    value = value.strip().lower()

    if value in ["yes", "y", "true", "1"]:
        return True

    if value in ["no", "n", "false", "0"]:
        return False

    raise ValueError("Please use yes or no.")


def ask_yes_no(question):
    """Ask a yes/no question and return True or False."""

    while True:
        answer = input(question + " (yes/no): ")

        try:
            parsed_answer = normalize_yes_no(answer)
            if parsed_answer is not None:
                return parsed_answer
        except ValueError:
            print("Please answer yes or no.")


def calculate_score_from_answers(answers):
    """Calculate lead score from a dictionary of answers."""

    score = 0

    for key, points in SCORING_RULES.items():
        if answers.get(key):
            score += points

    return score


def calculate_interactive_score():
    """Calculate lead score using interactive yes/no questions."""

    print("\nB2B Lead Score Calculator")
    print("-------------------------")
    print("Answer the following questions to estimate lead quality.\n")

    answers = {}

    for key, question in QUESTIONS.items():
        answers[key] = ask_yes_no(question)

    return calculate_score_from_answers(answers)


def classify_lead(score):
    """Classify lead quality based on total score."""

    if score >= 80:
        return "Hot lead"

    if score >= 60:
        return "Qualified lead"

    if score >= 40:
        return "Nurture lead"

    if score >= 20:
        return "Low-priority lead"

    return "Unqualified lead"


def recommend_next_step(score):
    """Recommend next action based on lead score."""

    if score >= 80:
        return "Prepare a quotation or move quickly to detailed sales follow-up."

    if score >= 60:
        return "Ask for any missing details, then prepare an item-based quotation."

    if score >= 40:
        return "Nurture the lead and ask qualification questions before quoting."

    if score >= 20:
        return "Ask for company information, quantity, delivery city, and buying purpose before sharing pricing."

    return "Do not send detailed pricing yet. Request basic information first."


def print_result(score):
    """Print lead score result."""

    classification = classify_lead(score)
    recommendation = recommend_next_step(score)

    print("\nResult")
    print("------")
    print(f"Lead score: {score}/100")
    print(f"Lead classification: {classification}")
    print(f"Recommended next step: {recommendation}")


def build_parser():
    """Build command-line argument parser."""

    parser = argparse.ArgumentParser(
        description="Calculate a B2B lead score based on qualification signals."
    )

    parser.add_argument("--company", help="Company information provided: yes/no")
    parser.add_argument("--product", help="Clear product requirement mentioned: yes/no")
    parser.add_argument("--quantity", help="Quantity mentioned: yes/no")
    parser.add_argument("--delivery", help="Delivery city or country mentioned: yes/no")
    parser.add_argument("--role", help="Contact role is relevant: yes/no")
    parser.add_argument("--urgency", help="Urgency or timeline mentioned: yes/no")
    parser.add_argument("--communication", help="Communication is professional and clear: yes/no")

    return parser


def parse_cli_answers(args):
    """Parse command-line answers into a dictionary."""

    raw_answers = {
        "company": args.company,
        "product": args.product,
        "quantity": args.quantity,
        "delivery": args.delivery,
        "role": args.role,
        "urgency": args.urgency,
        "communication": args.communication,
    }

    answers = {}

    for key, value in raw_answers.items():
        answers[key] = normalize_yes_no(value)

    return answers


def has_cli_input(args):
    """Check whether any command-line scoring arguments were provided."""

    return any(
        [
            args.company,
            args.product,
            args.quantity,
            args.delivery,
            args.role,
            args.urgency,
            args.communication,
        ]
    )


def main():
    """Run the lead score calculator."""

    parser = build_parser()
    args = parser.parse_args()

    try:
        if has_cli_input(args):
            answers = parse_cli_answers(args)

            missing_fields = [key for key, value in answers.items() if value is None]

            if missing_fields:
                print("Missing answers for:")
                for field in missing_fields:
                    print(f"- {field}")
                print("\nPlease provide yes/no values for all scoring criteria.")
                return

            score = calculate_score_from_answers(answers)

        else:
            score = calculate_interactive_score()

        print_result(score)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

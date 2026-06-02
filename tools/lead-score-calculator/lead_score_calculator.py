"""
Lead Score Calculator

A simple lead qualification tool for B2B exporters and global sales teams.

This tool helps salespeople estimate lead quality before sending a quotation,
catalog, full price list, or follow-up message.

Scoring logic:
- Company information provided: 15 points
- Clear product requirement: 20 points
- Quantity mentioned: 20 points
- Delivery city mentioned: 10 points
- Contact role is relevant: 15 points
- Urgency or timeline mentioned: 10 points
- Communication quality is professional: 10 points

Total score: 100 points
"""


def ask_yes_no(question):
    """Ask a yes/no question and return True or False."""
    while True:
        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True
        if answer in ["no", "n"]:
            return False

        print("Please answer yes or no.")


def calculate_lead_score():
    """Calculate lead score based on basic B2B qualification criteria."""

    print("\nB2B Lead Score Calculator")
    print("-------------------------")
    print("Answer the following questions to estimate lead quality.\n")

    score = 0

    if ask_yes_no("Did the customer provide company information?"):
        score += 15

    if ask_yes_no("Did the customer mention a clear product requirement?"):
        score += 20

    if ask_yes_no("Did the customer mention quantity?"):
        score += 20

    if ask_yes_no("Did the customer mention delivery city or country?"):
        score += 10

    if ask_yes_no("Is the contact role relevant to purchasing or decision-making?"):
        score += 15

    if ask_yes_no("Did the customer mention urgency or timeline?"):
        score += 10

    if ask_yes_no("Is the communication professional and clear?"):
        score += 10

    return score


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


def main():
    """Run the lead score calculator."""

    score = calculate_lead_score()
    classification = classify_lead(score)
    recommendation = recommend_next_step(score)

    print("\nResult")
    print("------")
    print(f"Lead score: {score}/100")
    print(f"Lead classification: {classification}")
    print(f"Recommended next step: {recommendation}")


if __name__ == "__main__":
    main()

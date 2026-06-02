# Lead Score Calculator

A simple command-line lead qualification tool for B2B exporters and global sales teams.

This tool helps salespeople estimate lead quality before sending a quotation, catalog, full price list, or follow-up message.

## What This Tool Does

The Lead Score Calculator asks a series of yes/no questions about a potential customer and calculates a lead score from 0 to 100.

It helps sales teams decide whether to:

* Prepare a quotation
* Ask more qualification questions
* Send selected catalog pages
* Avoid sending a full price list too early
* Nurture the lead
* Stop following low-quality leads

## Scoring Logic

The score is based on 7 qualification signals:

| Criteria                                                  | Points |
| --------------------------------------------------------- | -----: |
| Company information provided                              |     15 |
| Clear product requirement                                 |     20 |
| Quantity mentioned                                        |     20 |
| Delivery city or country mentioned                        |     10 |
| Contact role is relevant to purchasing or decision-making |     15 |
| Urgency or timeline mentioned                             |     10 |
| Communication is professional and clear                   |     10 |
| Total                                                     |    100 |

## Lead Classification

|  Score | Classification    |
| -----: | ----------------- |
| 80-100 | Hot lead          |
|  60-79 | Qualified lead    |
|  40-59 | Nurture lead      |
|  20-39 | Low-priority lead |
|   0-19 | Unqualified lead  |

## How to Run

Make sure Python is installed on your computer.

From this folder, run:

```
python lead_score_calculator.py
```

Then answer each question with:

```
yes
```

or:

```
no
```

The tool will return:

* Lead score
* Lead classification
* Recommended next step

## Example

Example input:

```
Did the customer provide company information? yes
Did the customer mention a clear product requirement? yes
Did the customer mention quantity? no
Did the customer mention delivery city or country? yes
Is the contact role relevant to purchasing or decision-making? yes
Did the customer mention urgency or timeline? no
Is the communication professional and clear? yes
```

Example result:

```
Lead score: 70/100
Lead classification: Qualified lead
Recommended next step: Ask for any missing details, then prepare an item-based quotation.
```

## When to Use This Tool

Use it when you receive leads from:

* Facebook ads
* LinkedIn outreach
* WhatsApp inquiries
* Website forms
* Exhibitions
* Referrals
* Cold outreach replies

## Important Notes

This tool is a decision-support tool, not a final judgment.

A low score does not always mean the lead is fake or useless. It may simply mean that more information is needed before quotation.

Do not use the score to make unfair assumptions about individuals or companies.

Always combine the score with:

* Company background research
* Buyer intent analysis
* Contact role analysis
* Salesperson judgment

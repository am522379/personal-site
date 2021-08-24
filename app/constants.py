
import os
import random


GOODREADS_ROOT = 'https://www.goodreads.com/book/show/'

skills = [
			{
				"name": "Financial Analysis: Asset Allocation, Personal Finance",
				"score": "95"
			},
			{
				"name": "Visual Basic for Applications (VBA)",
				"score": "95"
			},
						{
				"name": "Men's Style",
				"score": "82"
			},
			{
				"name": "Data Visualization",
				"score": "70"
			},
			{
				"name": "Python",
				"score": "65"
			},
			{
				"name": "SQL",
				"score": "60"
			},
			{
				"name": "Photography",
				"score": "55"
			}
		]

interests = [
			{
				"icon": "linegraph",
				"name": "Investing",
				"description": "test me"
			},
			{
				"icon": "laptop3",
				"name": "Computer Programming",
				"description": "test me"
			},
			{
				"icon": "wallet2",
				"name": "Personal Finance",
				"description": "test me"
			},
			{
				"icon": "camera3",
				"name": "Photography",
				"description": "Starting my style blog forced me to learn about photography. Soon after, photography and photo editing developed into a hobby. Using a Nikon D5300, I capture landscapes, city scapes, and candid portraits."
			},
			{
				"icon": "man",
				"name": "Men's Style",
				"description": "Style (as opposed to Fashion), stands the test of time. I love the idea of a wardobe that is sophisticated, simple, and built with a few high-quality, versatile peices."
			},
			{
				"icon": "wine",
				"name": "Cooking",
				"description": ""
			},
	]

education = [
				{
					"year": "2009-2013",
					"school": "Saint Joseph's University",
					"major": "Bachelor of Science, Finance and Business Intelligence",
					"achievements": "Summa Cum Laude"
				},
				{
					"year": "2005-2009",
					"school": "North Penn",
					"major": "",
					"achievements": ""
				},
			]

certifications = [
					{
						"institution": "CFA Institute",
						"cert": "CFA Charterholder",
						"cert_id": "ID#: 6998388"
					},
					{
						"institution": "CFP Board",
						"cert": "Certified Financial Planner Professional",
						"cert_id": "ID#: 325850"
					},
					{
						"institution": "FINRA",
						"cert": "Series 7",
						"cert_id": ""
					},
				]

experiences = [
					{
						"year": "August 2018 - Present",
						"company": "Moneyskope",
						"role": "CEO, Founder, and Money Coach",
						"description": "Launched a personal financial consultancy helping millenials pay down debt, save for their goals, and get smarter about money"
					},
					{
						"year": "August 2018 - Present",
						"company": "Vanguard",
						"role": "Investment Analyst",
						"description": "Enable non-profits and endowments to better achieve their mission by providing them with investment management advice"
					},
					{
						"year": "July 2017 - April 2019",
						"company": "With Aplomb",
						"role": "CEO, Founder, and Style Blogger",
						"description": "Hosted a men's style blog encouraging men to dress well by owning a few high-quality, versatile peices of clothing"
					},
					{
						"year": "August 2016 - August 2018",
						"company": "Vanguard",
						"role": "Investment Management Developer",
						"description": "Built financial models and portfolio management tools for the Fixed Income and Equity trading desks"
					},
					{
						"year": "June 2013 - April 2016",
						"company": "Vanguard",
						"role": "Fund Financial Analyst",
						"description": "Determined the valuation of Fixed Income securities and built department-wide process improvements"
					},
				]

books = [
			{
				"link": f'{GOODREADS_ROOT}771063.The_Metaphysics',
				"file": "metaphysics",
				"title": "Metaphysics",
				"author": "Aristotle",
				"description": ""
			},
			{
				"link": f'{GOODREADS_ROOT}7785194-the-moral-landscape',
				"file": "the_moral_landscape",
				"title": "The Moral Landscape",
				"author": "Sam Harris",
				"description": "How Science Can Determine Human Values"
			},
			{
				"link": f'{GOODREADS_ROOT}12987640-imagine',
				"file": "imagine",
				"title": "Imagine",
				"author": "Jonah Lehrer",
				"description": "How Creativity Works"
			},
			{
				"link": f'{GOODREADS_ROOT}6346975-moonwalking-with-einstein',
				"file": "moonwalking_with_einstein",
				"title": "Moonwalking with Einstein",
				"author": "Joshua Foer",
				"description": "The Art and Science of Remembering Everything"
			},
			{
				"link": f'{GOODREADS_ROOT}44770129-ultralearning',
				"file": "ultralearning",
				"title": "Ultralearning",
				"author": "Scott H. Young",
				"description": "Master Hard Skills, Outsmart the Competition, and Accelerate Your Career"
			},
			{
				"link": f'{GOODREADS_ROOT}13588356-daring-greatly',
				"file": "daring_greatly",
				"title": "Daring Greatly",
				"author": "Brene Brown",
				"description": "How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead"
			},
			{
				"link": f'{GOODREADS_ROOT}32938155-option-b',
				"file": "option_b",
				"title": "Option B",
				"author": "Sheryl Sandberg",
				"description": "Facing Adversity, Building Resilience, and Finding Joy"
			}
		]


def obtain_gallery():

	ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
	path = ROOT_DIR + '/static/images/gallery/'

	JPG = '.jpg'

	g = []

	for filename in os.listdir(path=path):
		if filename.endswith(JPG):
			fname = filename[:-len(JPG)]
			tag = fname[fname.rfind('_') + 1:]
			title = fname[:fname.rfind('_')]

			if title.find('_') > 0:
				title = title.replace('_', ' ')

			if title[-1].isdigit():
				title = title[:-1]

			title = title.title()

			photo = {
						'file': fname,
						'title': title ,
						'category': tag
					}

			g.append(photo)

	random_gallery = random.sample(g, k=9)

	return random_gallery

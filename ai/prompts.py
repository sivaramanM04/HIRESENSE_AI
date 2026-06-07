def technical_question_prompt(
        role,
        difficulty
):

    return f"""

You are a senior technical interviewer.

Conduct a {role} interview.

Difficulty level:
{difficulty}

Generate ONE interview question.

Rules:
- Ask only one question
- Don't give answer
- Behave like real interviewer

"""


def evaluate_answer_prompt(
        question,
        answer
):

    return f"""

You are a strict technical interviewer.

Question:
{question}


Candidate Answer:
{answer}


Evaluate the candidate.

Give output format:


Score:
__/10


Strengths:
-


Mistakes:
-


Correct Answer:
-


Next Improvement:
-

"""

def resume_analysis_prompt(resume_text):

    return f"""

You are HireSense AI Resume Analyzer.

Act as:
- Senior HR
- ATS System
- Technical Recruiter


Analyze this resume:


{resume_text}



Give output in this format:


ATS SCORE:
__/100


PROFILE SUMMARY:
...


TECHNICAL SKILLS FOUND:
-


MISSING SKILLS:
-


PROJECT ANALYSIS:
-


RESUME MISTAKES:
-


IMPROVEMENTS:
-


BEST SUITABLE JOB ROLES:
-


GENERATE 5 INTERVIEW QUESTIONS FROM THIS RESUME:
1.
2.
3.
4.
5.

"""

def resume_interview_prompt(
        context,
        role
):


    return f"""

You are an expert interviewer.

You are interviewing candidate for:

{role}


Use ONLY this resume information:


{context}



Generate:

5 personalized interview questions.

Questions should include:

- Projects
- Skills
- Experience
- Technologies


Don't ask generic questions.


"""

def hr_question_prompt(
        experience,
        role
):

    return f"""

You are a professional HR interviewer.

You are interviewing a candidate.

Role:
{role}

Experience:
{experience}


Generate only ONE HR interview question.

Rules:
- Don't give answer
- Ask like a real HR
- Keep question professional

"""



def hr_answer_evaluation_prompt(
        question,
        answer
):

    return f"""

You are a senior HR manager.

Analyze this interview answer.


Question:

{question}


Candidate Answer:

{answer}



Evaluate:


Overall Score:
/10


Communication Score:
/10


Confidence Score:
/10


Strengths:
-


Weakness:
-


Mistakes:
-


Improved Professional Answer:
-


Selection Probability:
__%

"""

def mock_interview_prompt(answer):

    return f"""

You are an AI interview evaluator.

Analyze this spoken interview answer:


Candidate:

{answer}


Evaluate:


Technical Knowledge:
/10


Communication:
/10


Confidence:
/10


Fluency:
/10


Mistakes:
-


Suggestions:
-


Final Selection Chance:
%

"""

def code_review_prompt(problem, code):

    return f"""

You are a senior software engineer conducting
a coding interview.

Problem:

{problem}


Candidate Code:

{code}


Analyze this solution.


Return:


Correctness Score:
/10


Code Quality:
/10


Time Complexity:
Big O


Space Complexity:
Big O


Bugs:
-


Optimization:
-


Better Approach:
-


Interview Feedback:
-


Hiring Decision:
Selected / Need Improvement


"""

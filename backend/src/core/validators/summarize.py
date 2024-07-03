from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def message_summary(message:str) -> (str):
    result = summarizer(message, max_length=20, min_length=1, do_sample=False)
    summary = result[0]['summary_text']
    return summary

if __name__ == "__main__":
    ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
    A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
    Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
    In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
    Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
    2010 marriage license application, according to court documents.
    Prosecutors said the marriages were part of an immigration scam.
    On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
    After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
    Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
    All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
    Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
    Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
    The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
    Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
    Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
    If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
    """
    # "I am trying to solve many problems of my business. The goals of the app is I want to market my salon. So anyone who knows the name of my salon can browse and checkout what we offer. and also rather than showing up all of a sudden to get services or calling all the time and scheduling or coming to the salon to schedule, I think it will be easier if we can let them book appointments before coming to the salon. Even without booking they can come, but they may have to leave if we're not available when they're coming. So we want to solve that problem by letting them book online. and also they will be able to see the things we offer. That way rather than depending on what they've heard or making call all the time, they can checkout our website"
    # "I want to let the users book appointments by giving their convenient date and time as an input. You can let them chose through a calendar and time selector or just as an input, anyway you like. There is no need to consider our employee availability, users just have to input date, time. NIC number and email so that we can contact them regarding the appointment."
    print(f"Summary: {message_summary(ARTICLE)}")

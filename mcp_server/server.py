from fastmcp import FastMCP

mcp = FastMCP("COD Document Server")

# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

PARTICIPANT_ID = "1012345678V123456"  # Samuel Murphy's ICN

DOCUMENTS = {
    "DOC001": {
        "document_id": "DOC001",
        "participant_id": PARTICIPANT_ID,
        "document_type": "DD214",
        "title": "Certificate of Release or Discharge from Active Duty",
        "date": "2003-08-15",
        "source": "DPRIS",
    },
    "DOC002": {
        "document_id": "DOC002",
        "participant_id": PARTICIPANT_ID,
        "document_type": "Military Personnel Record",
        "title": "Service Record – Disciplinary Actions",
        "date": "2003-07-01",
        "source": "NPRC",
    },
    "DOC003": {
        "document_id": "DOC003",
        "participant_id": PARTICIPANT_ID,
        "document_type": "VA Form 21-0781",
        "title": "Statement in Support of Claim for PTSD",
        "date": "2023-03-10",
        "source": "VBMS",
    },
    "DOC004": {
        "document_id": "DOC004",
        "participant_id": PARTICIPANT_ID,
        "document_type": "Buddy Statement",
        "title": "Personal Statement – Carlos Rivera",
        "date": "2023-04-02",
        "source": "VBMS",
    },
    "DOC005": {
        "document_id": "DOC005",
        "participant_id": PARTICIPANT_ID,
        "document_type": "Administrative Decision",
        "title": "Character of Discharge Determination – Initial Decision",
        "date": "2023-06-20",
        "source": "VBMS",
    },
}

DOCUMENT_TEXT = {
    "DOC001": """\
CERTIFICATE OF RELEASE OR DISCHARGE FROM ACTIVE DUTY (DD Form 214)

1. NAME (Last, First, Middle): Murphy, Samuel James
2. DEPARTMENT/COMPONENT/BRANCH: Army
3. SOCIAL SECURITY NO.: XXX-XX-7821
4. DATE OF BIRTH: 19780413
5. DATE OF ENTRY ON ACTIVE DUTY: 20010312
6. HOME OF RECORD AT TIME OF ENTRY: 412 Oak Street, Columbus, OH 43215

9. COMMAND TO WHICH TRANSFERRED: NA – Discharge

11. PRIMARY SPECIALTY: 11B – Infantryman (26 months)

12. RECORD OF SERVICE
    a. Date Entered AD This Period: 2001-03-12
    b. Separation Date This Period: 2003-08-15
    c. Net Active Service This Period: 2 years, 5 months, 3 days
    d. Total Prior Active Service: NONE
    e. Total Prior Inactive Service: NONE

13. DECORATIONS, MEDALS, BADGES, CITATIONS AND CAMPAIGN RIBBONS AWARDED OR AUTHORIZED:
    Army Service Ribbon; National Defense Service Medal; Global War on Terrorism Service Medal

23. TYPE OF SEPARATION: Discharge

24. CHARACTER OF SERVICE: Under Other Than Honorable Conditions (UOTHC)

25. SEPARATION AUTHORITY: AR 635-200, Chapter 14

26. SEPARATION CODE: 385 – Absent Without Leave (AWOL) / Desertion

27. REENTRY CODE: RE-4

28. NARRATIVE REASON FOR SEPARATION: Misconduct – Absent Without Leave

REMARKS:
Soldier departed Absent Without Leave on 2003-02-14 from Fort Bragg, NC.
Returned to military control 2003-06-01. Tried by Summary Court-Martial.
Discharged Under Other Than Honorable Conditions per AR 635-200, Chapter 14-12b.
""",

    "DOC002": """\
MILITARY PERSONNEL RECORD – DISCIPLINARY ACTIONS
Name: Murphy, Samuel James  |  SSN: XXX-XX-7821  |  Unit: 3rd Battalion, 505th PIR, 82nd Airborne Division

SERVICE HISTORY SUMMARY:
- Enlisted: 12 March 2001, Fort Benning, GA
- MOS: 11B (Infantryman)
- Deployed: Operation Enduring Freedom, Afghanistan, Sep 2001 – Mar 2002
- Returned to Fort Bragg, NC: April 2002

COUNSELING STATEMENTS:
1. Date: 2002-09-15
   Reason: Failure to report to formation on time (3 occurrences within 60 days)
   Action: Verbal counseling; no further action taken.

2. Date: 2002-12-03
   Reason: Alcohol-related incident off post; public intoxication
   Action: Article 15 (Non-Judicial Punishment); reduction in rank from SPC (E-4) to PFC (E-3); forfeiture of $300 pay for one month.

3. Date: 2003-01-20
   Reason: Unauthorized absence from unit for 48 hours
   Action: Letter of Reprimand filed in Official Military Personnel File.

AWOL RECORD:
- Date departed AWOL: 14 February 2003
- Duration: 107 days
- Date returned to military control: 01 June 2003, Fort Bragg, NC (surrendered voluntarily)

COURT-MARTIAL:
- Type: Summary Court-Martial
- Date: 25 June 2003
- Charge: Violation of UCMJ Article 86 – Absent Without Leave (>30 days)
- Plea: Guilty
- Sentence: Forfeiture of 2/3 pay for 1 month; no confinement imposed.

SEPARATION PROCEEDINGS:
- Chapter 14-12b initiated by unit commander CPT Rodriguez on 02 July 2003.
- Soldier waived right to an administrative separation board.
- Approved by separation authority: 10 August 2003.
- Effective date of discharge: 15 August 2003.
- Character of Discharge: Under Other Than Honorable Conditions.

MEDICAL NOTES ON FILE:
- Behavioral Health referral noted: 2002-11-10. Soldier reported difficulty sleeping and heightened anxiety following return from Afghanistan. Attended 2 of 6 scheduled sessions before disengaging from care.
""",

    "DOC003": """\
VA FORM 21-0781 – STATEMENT IN SUPPORT OF CLAIM FOR PTSD
Veteran: Murphy, Samuel James  |  VA File No.: 21-000-7821  |  Date Submitted: 10 March 2023

SECTION I – STRESSOR INFORMATION

Stressor 1:
Date: October 2001 – February 2002
Location: Kandahar Province, Afghanistan
Unit: 3/505 PIR, 82nd Airborne Division
Description:
During a foot patrol near Kandahar City on or about November 18, 2001, our unit came under an ambush. IED detonated approximately 10 meters from my position. Private First Class D. Holloway, who was walking directly ahead of me, was killed instantly. I was knocked off my feet and regained consciousness to find him deceased. I rendered aid but was unable to save him. This event has recurred in my nightmares since that day. I was never provided counseling for this incident.

Stressor 2:
Date: January 2002
Location: FOB Salerno, Khost Province, Afghanistan
Unit: 3/505 PIR, 82nd Airborne Division
Description:
On or about January 9, 2002, a mortar attack struck our FOB during evening meal. Three soldiers in my platoon were wounded. I assisted in casualty evacuation under continued fire. The smell of burning and the sound of incoming rounds remain my most persistent triggers today.

SECTION II – VETERAN STATEMENT

After returning from Afghanistan in April 2002, I was not the same person. I could not sleep. I drank heavily to quiet my mind. I isolated from my unit and my family. I missed formations because I could not get out of bed some mornings. I knew I needed help but felt ashamed to ask for it. When I did go to Behavioral Health in November 2002, I stopped going after two sessions because I did not feel safe talking about what I saw.

By February 2003 I could not function. I left the base without telling anyone. I was not trying to desert – I was trying to survive. I drove home to Columbus and stayed with my mother for three months. I was not hiding from the Army. I was hiding from what was in my own head. I came back on my own because I knew I had to face it.

I was discharged Under Other Than Honorable Conditions. I accept responsibility for leaving without authorization. But I ask that the VA consider that my absence was a direct result of untreated trauma from my combat service.

I was diagnosed with PTSD by Dr. Anita Sharma at the Columbus Vet Center on January 14, 2023 (records attached separately).

I am requesting that my discharge be upgraded so that I may receive the benefits I need to continue my treatment.

Signature: Samuel J. Murphy  |  Date: 2023-03-10
""",

    "DOC004": """\
BUDDY STATEMENT – PERSONAL STATEMENT IN SUPPORT OF SAMUEL MURPHY
Submitted by: Carlos Rivera, Former SPC, 3/505 PIR, 82nd Airborne Division
Date: 02 April 2023

I served alongside Samuel Murphy from the time we enlisted together at Fort Benning in March 2001 through our deployment to Afghanistan and until his discharge in 2003. I am submitting this statement because I believe Sam's discharge does not reflect who he was as a soldier or what he went through.

Sam was one of the most motivated guys in our platoon before we deployed. He was always early to formation, always helping junior soldiers. When we got to Afghanistan, he did everything asked of him without complaint.

Everything changed after the ambush in November 2001 where PFC Holloway was killed. Sam was right there. He tried to save him. After that day, Sam was different. He didn't talk much. He stopped eating with the rest of us. He started waking up screaming at night. We all saw it, but none of us knew what to say. Back then, you didn't talk about that stuff. You just pushed through.

When we got back to Bragg in April 2002, Sam tried to keep going but it was clear he was struggling. He started drinking. He missed a few formations. The Army gave him an Article 15, which only made things worse. He went to Behavioral Health a couple of times but said it wasn't helping.

When he went AWOL in February 2003, I was not surprised. He had told me a few weeks before that he felt like he was going to lose his mind if he stayed. He was not trying to dodge his duties. He was in crisis.

I have no doubt that Sam's absence was a direct result of the untreated psychological wounds he suffered in combat. He was a good soldier who fell through the cracks of a system that did not have the tools to help him at the time.

I respectfully request that the VA consider these circumstances when evaluating his discharge characterization.

Signed: Carlos Rivera  |  Phone: (614) 555-0182  |  Date: 2023-04-02
""",

    "DOC005": """\
CHARACTER OF DISCHARGE DETERMINATION – INITIAL ADMINISTRATIVE DECISION
VA Regional Office: Columbus, OH  |  VA File No.: 21-000-7821  |  Date: 20 June 2023
Veteran: Murphy, Samuel James  |  DOB: 13 April 1978

ISSUE PRESENTED:
Whether the veteran's discharge Under Other Than Honorable Conditions (UOTHC) constitutes a bar to VA benefits under 38 U.S.C. § 5303 and 38 C.F.R. § 3.12.

SUMMARY OF FACTS:
The veteran served in the U.S. Army from March 12, 2001 to August 15, 2003. He was separated under AR 635-200, Chapter 14-12b for Misconduct (AWOL) with a character of service of Under Other Than Honorable Conditions. The period of AWOL lasted 107 days (February 14, 2003 – June 1, 2003). The veteran was tried by Summary Court-Martial and pled guilty to violation of UCMJ Article 86.

APPLICABLE LAW:
Under 38 C.F.R. § 3.12(c)(6), a dishonorable discharge or a discharge under other than honorable conditions issued as a result of AWOL for a continuous period of at least 180 days constitutes a statutory bar to benefits. The veteran's AWOL period was 107 days, which does not meet the 180-day threshold for a statutory bar.

However, under 38 C.F.R. § 3.12(d), the VA must further evaluate whether the discharge was issued under dishonorable conditions, considering the veteran's overall service record and the circumstances of the separation.

ANALYSIS:
The veteran's AWOL does not trigger the statutory bar under § 3.12(c)(6) given its duration of 107 days. Under § 3.12(d), this office must weigh the character of the veteran's entire service.

Factors weighing against:
- AWOL of 107 days represents a significant breach of military duty.
- Summary Court-Martial conviction for UCMJ Article 86.
- Prior Article 15 and counseling statements for related misconduct.

Factors weighing in favor:
- Honorable service during combat deployment (OEF, Sep 2001 – Mar 2002).
- No prior criminal history.
- Behavioral Health referral in November 2002 suggests early indicators of mental health difficulty.
- Veteran submitted VA Form 21-0781 citing combat stressors; PTSD diagnosis from licensed provider dated January 2023 is on file.
- Veteran voluntarily surrendered to military control.

DECISION:
This office finds that, on the current record, the veteran's discharge was issued under dishonorable conditions per 38 C.F.R. § 3.12(d), and his claim is denied at this time. However, this decision is non-final. The veteran may submit additional evidence, including nexus evidence linking his AWOL to service-connected mental health conditions, within one year of this decision.

NOTE FOR REVIEWING RATER:
This case may qualify for liberal consideration under the Kurta Memo (2018) if a nexus between the misconduct and a service-connected mental health condition (PTSD) can be established. An Integrated Disability Evaluation System (IDES) or Mental Health Review is recommended before final adjudication.

Signed: Regional Office Adjudicator, Columbus VARO  |  Date: 2023-06-20
""",
}


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def search(participant_id: str) -> list[dict]:
    """Search for documents associated with a veteran participant ID.

    Returns a list of document metadata records. Use retrieve_text_content
    with a document_id to fetch the full text of any document.
    """
    results = [
        doc for doc in DOCUMENTS.values()
        if doc["participant_id"] == participant_id
    ]
    if not results:
        return []
    return results


@mcp.tool()
def retrieve_text_content(document_id: str) -> str:
    """Retrieve the full text content of a document by its document_id."""
    if document_id not in DOCUMENT_TEXT:
        return f"Error: document '{document_id}' not found."
    return DOCUMENT_TEXT[document_id]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()

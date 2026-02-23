# COD Case Analysis — Samuel Murphy (v3 Final)
**Participant ID:** 1012345678V123456
**Analysis Date:** 2026-02-23
**Pipeline:** cod-agent (search + retrieve) → cod-summarizer (summarize, uniform)
**Summarization Model:** claude-haiku-4-5-20251001
**Extraction Focus:** Character of Discharge determination: extract character of discharge designation, separation authority and code, discharge reason, RE code, service dates, disciplinary actions, mental health references, mitigating factors, and awards

---

## Step 1 — Search Results

`cod-agent.search(participant_id="1012345678V123456")` returned 8 documents:

| Doc ID | Type | Title | Date | Source |
|---|---|---|---|---|
| DOC001 | DD214 | Certificate of Release or Discharge from Active Duty | 2003-08-15 | DPRIS |
| DOC002 | Military Personnel Record | Service Record – Disciplinary Actions | 2003-07-01 | NPRC |
| DOC003 | VA Form 21-0781 | Statement in Support of Claim for PTSD | 2023-03-10 | VBMS |
| DOC004 | Buddy Statement | Personal Statement – Carlos Rivera | 2023-04-02 | VBMS |
| DOC005 | Administrative Decision | Character of Discharge Determination – Initial Decision | 2023-06-20 | VBMS |
| DOC006 | VA Medical Record | Annual Health Examination | 2023-09-14 | VistA |
| DOC007 | VA Form 22-1999 | Post-9/11 GI Bill Enrollment Certification | 2023-07-25 | WAVE |
| DOC008 | VA Form 26-8320 | Certificate of Eligibility – Home Loan Guaranty | 2024-03-06 | LGY |

---

## Step 2 — Raw Text Retrieved

All 8 documents retrieved via `cod-agent.retrieve_text_content(document_id)` in parallel.

---

## Step 3 — Summaries (cod-summarizer, uniform)

### DOC001 — DD214
**Character of Discharge:** Under Other Than Honorable Conditions (UOTHC)
**Separation Authority:** AR 635-200, Chapter 14
**Separation Code:** 385 – Absent Without Leave / Desertion
**RE Code:** RE-4
**Service Dates:** 2001-03-12 → 2003-08-15 (2 years, 5 months, 3 days)
**Disciplinary Actions:** AWOL from Fort Bragg, NC 2003-02-14; returned to military control 2003-06-01; tried by Summary Court-Martial
**Mental Health References:** None present in document
**Mitigating Factors:** None documented
**Awards:** Army Service Ribbon; National Defense Service Medal; Global War on Terrorism Service Medal

---

### DOC002 — Military Personnel Record / Disciplinary Actions
**Character of Discharge:** Under Other Than Honorable Conditions
**Separation Authority:** AR 635-200, Chapter 14-12b; initiated by CPT Rodriguez 2003-07-02; approved 2003-08-10
**Separation Code:** Not stated
**RE Code:** Not specified
**Service Dates:** Enlisted 2001-03-12; discharged 2003-08-15; OEF deployment Sep 2001 – Mar 2002
**Disciplinary Actions:**
1. 2002-09-15 — Verbal counseling (failure to report to formation, 3 occurrences in 60 days)
2. 2002-12-03 — Article 15 NJP (public intoxication off-post); rank reduced E-4 → E-3; $300 pay forfeiture
3. 2003-01-20 — Letter of Reprimand (48-hr unauthorized absence)
4. 2003-06-25 — Summary Court-Martial; guilty plea, UCMJ Art. 86 (AWOL >30 days); 2/3 pay forfeiture, no confinement
5. AWOL: 2003-02-14 → 2003-06-01 (107 days); voluntarily surrendered

**Mental Health References:** BH referral 2002-11-10; reported sleep difficulty and heightened anxiety post-OEF deployment; attended 2 of 6 scheduled sessions before disengaging
**Mitigating Factors:** Post-deployment mental health symptoms documented; voluntary return from AWOL
**Awards:** None noted in document

---

### DOC003 — VA Form 21-0781 / PTSD Stressor Statement
**Character of Discharge:** UOTHC (self-reported)
**Separation Authority / Code / RE Code:** Not in document
**Discharge Reason:** Unauthorized absence Feb 2003; ~3 months duration; voluntary return
**Service Dates:** OEF Oct 2001 – Apr 2002 (Kandahar Province; Khost Province)
**Disciplinary Actions:** Unauthorized absence Feb–May 2003
**Mental Health References:** BH Nov 2002 (2 sessions, discontinued — felt unsafe); PTSD diagnosis Dr. Anita Sharma, Columbus Vet Center, 2023-01-14; symptoms: nightmares, insomnia, heavy alcohol use, social isolation, inability to maintain duties
**Mitigating Factors:**
- Combat stressor 1: IED ambush ~2001-11-18, Kandahar City; PFC D. Holloway KIA directly ahead of veteran; veteran rendered aid
- Combat stressor 2: Mortar attack ~2002-01-09, FOB Salerno; 3 soldiers wounded; veteran assisted CASEVAC under fire
- Untreated PTSD at time of AWOL; voluntary return; veteran accepts responsibility for absence

**Awards:** Not in document

---

### DOC004 — Buddy Statement (Carlos Rivera, SPC, 3/505 PIR)
**Character / Sep Authority / Code / RE Code:** Not in document (lay statement)
**Service Dates:** Co-enlisted March 2001; OEF deployment; discharged 2003
**Disciplinary Actions:** Article 15 noted; AWOL Feb 2003 corroborated
**Mental Health References:** Witnessed behavioral changes post-ambush Nov 2001: insomnia with nightmares, social withdrawal, appetite loss, alcohol use; confirms BH attendance (stated ineffective)
**Mitigating Factors:** Pre-deployment exemplary performance (punctual, mentored junior soldiers); AWOL characterized as psychological crisis not duty avoidance; Murphy told Rivera he would "lose his mind" if he stayed; systemic failure to provide adequate MH support acknowledged
**Awards:** Not in document

---

### DOC005 — COD Initial Administrative Decision
**Character of Discharge:** UOTHC
**Separation Authority:** AR 635-200, Chapter 14-12b
**Discharge Reason:** Misconduct / AWOL 107 days (2003-02-14 → 2003-06-01)
**RE Code:** Not specified
**Service Dates:** 2001-03-12 → 2003-08-15; OEF Sep 2001 – Mar 2002
**Disciplinary Actions:** Summary Court-Martial (UCMJ Art. 86, guilty); prior Article 15; counseling statements
**Mental Health References:** BH referral Nov 2002; VA Form 21-0781 on file; PTSD diagnosis Jan 2023 from licensed provider
**Mitigating Factors:** Honorable combat service (OEF); no prior criminal history; early MH indicators (BH referral Nov 2002); voluntary surrender
**Decision:** Denied under 38 C.F.R. § 3.12(d) — non-final. Kurta Memo (2018) liberal consideration flagged; nexus evidence requested within one year.
**Awards:** Not specified

---

### DOC006 — VA Medical Record / Annual Health Exam
**COD Relevance:** None. Routine wellness exam 2023-09-14, Dr. Kevin Okafor, VA Medical Center Indianapolis. No discharge, disciplinary, or service-history content applicable to COD determination.

---

### DOC007 — VA Form 22-1999 / Post-9/11 GI Bill Enrollment
**COD Relevance:** None. Education benefit certification, Georgia State University MPA program, Fall 2023. No discharge or misconduct content.
**Contextual note:** GI Bill benefit access granted — some benefit eligibility has been established despite pending COD determination.

---

### DOC008 — VA Form 26-8320 / Home Loan Certificate of Eligibility
**COD Relevance:** None. VA Home Loan eligibility confirmed 2024-03-06, Denver VARLC. No discharge or misconduct content.
**Contextual note:** Home loan eligibility established — consistent with at least partial benefit access pending final COD adjudication.

---

## Step 7 — Final JSON Output

```json
{
  "analysis_metadata": {
    "participant_id": "1012345678V123456",
    "veteran_name": "Murphy, Samuel James",
    "dob": "1978-04-13",
    "va_file_no": "21-000-7821",
    "analysis_date": "2026-02-23",
    "pipeline": "cod-agent + cod-summarizer",
    "summarization_model": "claude-haiku-4-5-20251001",
    "documents_retrieved": 8,
    "documents_cod_relevant": 5,
    "documents_not_cod_relevant": 3
  },

  "discharge_facts": {
    "character_of_discharge": "Under Other Than Honorable Conditions (UOTHC)",
    "separation_authority": "AR 635-200, Chapter 14-12b",
    "separation_code": "385",
    "separation_code_description": "Absent Without Leave / Desertion",
    "narrative_reason": "Misconduct – Absent Without Leave",
    "re_code": "RE-4",
    "service_entry_date": "2001-03-12",
    "service_separation_date": "2003-08-15",
    "net_active_service": "2 years, 5 months, 3 days",
    "component_branch": "Army",
    "primary_mos": "11B – Infantryman",
    "source_document": "DOC001"
  },

  "awards_and_decorations": [
    "Army Service Ribbon",
    "National Defense Service Medal",
    "Global War on Terrorism Service Medal"
  ],

  "combat_service": {
    "operation": "Operation Enduring Freedom (OEF)",
    "theater": "Afghanistan (Kandahar Province; Khost Province)",
    "unit": "3rd Battalion, 505th PIR, 82nd Airborne Division",
    "period_start": "2001-09",
    "period_end": "2002-03",
    "source_documents": ["DOC002", "DOC003"]
  },

  "disciplinary_record": [
    {
      "date": "2002-09-15",
      "type": "Verbal Counseling",
      "reason": "Failure to report to formation (3 occurrences in 60 days)",
      "action": "Verbal counseling; no further action",
      "source": "DOC002"
    },
    {
      "date": "2002-12-03",
      "type": "Article 15 (NJP)",
      "reason": "Alcohol-related incident off post; public intoxication",
      "action": "Rank reduced E-4 to E-3; forfeiture of $300 pay for one month",
      "source": "DOC002"
    },
    {
      "date": "2003-01-20",
      "type": "Letter of Reprimand",
      "reason": "Unauthorized absence from unit for 48 hours",
      "action": "LOR filed in OMPF",
      "source": "DOC002"
    },
    {
      "date": "2003-02-14",
      "type": "AWOL",
      "reason": "Departed AWOL from Fort Bragg, NC",
      "duration_days": 107,
      "returned": "2003-06-01",
      "return_circumstances": "Voluntary surrender",
      "source": "DOC001, DOC002"
    },
    {
      "date": "2003-06-25",
      "type": "Summary Court-Martial",
      "charge": "UCMJ Article 86 – Absent Without Leave (>30 days)",
      "plea": "Guilty",
      "sentence": "Forfeiture of 2/3 pay for one month; no confinement",
      "source": "DOC002"
    }
  ],

  "mental_health_record": [
    {
      "date": "2002-11-10",
      "event": "Behavioral Health referral",
      "detail": "Reported sleep difficulty and heightened anxiety following return from OEF; attended 2 of 6 scheduled sessions before disengaging",
      "source": "DOC002"
    },
    {
      "date": "2023-01-14",
      "event": "PTSD diagnosis",
      "provider": "Dr. Anita Sharma",
      "facility": "Columbus Vet Center",
      "detail": "Formal PTSD diagnosis; records filed separately with VA",
      "source": "DOC003"
    }
  ],

  "combat_stressors": [
    {
      "date": "2001-11-18",
      "location": "Kandahar City, Afghanistan",
      "description": "IED ambush during foot patrol; PFC D. Holloway KIA directly ahead of veteran; veteran rendered aid and was unable to save him",
      "source": "DOC003, DOC004"
    },
    {
      "date": "2002-01-09",
      "location": "FOB Salerno, Khost Province, Afghanistan",
      "description": "Mortar attack during evening meal; 3 soldiers wounded; veteran assisted CASEVAC under continued fire",
      "source": "DOC003"
    }
  ],

  "mitigating_factors": [
    "Honorable combat service during OEF (Sep 2001 – Mar 2002)",
    "Two documented in-theater traumatic stressors corroborated by buddy statement (DOC004)",
    "Behavioral Health referral on file predating AWOL (2002-11-10), indicating early MH distress recognized by military",
    "Formal PTSD diagnosis by licensed provider (2023-01-14) consistent with symptoms onset post-deployment",
    "AWOL characterized by veteran and corroborated by peer as psychological crisis, not desertion intent",
    "Voluntary surrender to military control (2003-06-01)",
    "No prior criminal history outside military context",
    "Pre-deployment exemplary performance noted by fellow servicemember (DOC004)"
  ],

  "statutory_bar_analysis": {
    "regulation": "38 C.F.R. § 3.12(c)(6)",
    "threshold_days": 180,
    "actual_awol_days": 107,
    "bar_triggered": false,
    "basis": "AWOL duration of 107 days does not meet 180-day continuous threshold for statutory bar to benefits"
  },

  "regulatory_bar_analysis": {
    "regulation": "38 C.F.R. § 3.12(d)",
    "current_finding": "Discharge found to have been issued under dishonorable conditions",
    "decision_date": "2023-06-20",
    "decision_status": "Non-final — open for supplemental evidence within one year of decision date",
    "source_document": "DOC005"
  },

  "kurta_memo_applicability": {
    "applicable": true,
    "basis": "PTSD diagnosis on file; documented combat stressors; pattern of misconduct (formation, alcohol, AWOL) consistent with untreated PTSD symptomatology",
    "nexus_formalized": false,
    "nexus_gap": "No formal nexus opinion linking PTSD diagnosis to AWOL episode is yet in file",
    "flagged_by": "VARO Columbus adjudicator, DOC005"
  },

  "benefit_access_signals": [
    {
      "benefit": "Post-9/11 GI Bill (Chapter 33)",
      "status": "Active — enrolled full-time, Georgia State University MPA, Fall 2023",
      "document": "DOC007"
    },
    {
      "benefit": "VA Home Loan Guaranty",
      "status": "Certificate of Eligibility issued 2024-03-06; full entitlement available ($181,550)",
      "document": "DOC008"
    },
    {
      "benefit": "VA Primary Care",
      "status": "Active — annual exam 2023-09-14, VA Medical Center Indianapolis",
      "document": "DOC006"
    }
  ],

  "documents_reviewed": [
    {"document_id": "DOC001", "type": "DD214", "date": "2003-08-15", "cod_relevant": true},
    {"document_id": "DOC002", "type": "Military Personnel Record", "date": "2003-07-01", "cod_relevant": true},
    {"document_id": "DOC003", "type": "VA Form 21-0781", "date": "2023-03-10", "cod_relevant": true},
    {"document_id": "DOC004", "type": "Buddy Statement", "date": "2023-04-02", "cod_relevant": true},
    {"document_id": "DOC005", "type": "Administrative Decision", "date": "2023-06-20", "cod_relevant": true},
    {"document_id": "DOC006", "type": "VA Medical Record", "date": "2023-09-14", "cod_relevant": false},
    {"document_id": "DOC007", "type": "VA Form 22-1999", "date": "2023-07-25", "cod_relevant": false},
    {"document_id": "DOC008", "type": "VA Form 26-8320", "date": "2024-03-06", "cod_relevant": false}
  ],

  "recommended_next_steps": [
    {
      "priority": 1,
      "action": "Obtain formal nexus opinion",
      "detail": "Secure a written medical opinion from Dr. Anita Sharma or a VA examiner establishing a nexus between the PTSD diagnosis (2023-01-14) and the AWOL episode (2003-02-14). This is the single most critical missing element for liberal consideration under the Kurta Memo."
    },
    {
      "priority": 2,
      "action": "Request Mental Health Review before final adjudication",
      "detail": "VARO adjudicator (DOC005) explicitly recommended an IDES or Mental Health Review prior to final decision. Ensure this is scheduled and completed."
    },
    {
      "priority": 3,
      "action": "Confirm one-year supplemental evidence deadline",
      "detail": "Initial decision was dated 2023-06-20. Supplemental evidence must be submitted within one year (by approximately 2024-06-20). Verify whether this deadline has been met or whether an extension / new claim is needed."
    },
    {
      "priority": 4,
      "action": "Attach Columbus Vet Center PTSD records",
      "detail": "VA Form 21-0781 (DOC003) references PTSD treatment records from Dr. Sharma as 'attached separately' but these were not among the 8 documents retrieved. Confirm they are on file in VBMS."
    }
  ],

  "agent_notes": "This analysis does not constitute a COD upgrade recommendation. All findings are presented for VSR review. The veteran has a plausible nexus theory supported by corroborating lay evidence; formalization of that nexus by a qualified medical provider is the key remaining evidentiary gap."
}
```

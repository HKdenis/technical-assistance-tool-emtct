import streamlit as st
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import datetime
import os

title = st.title("Technical Assistance/Mentorship Report")
st.markdown("""*MWP EMTCT Team*""")

# Use session_state keys for each widget so we can reset them after submission
selected_date = st.date_input("VISIT DATE:", format="DD/MM/YYYY", key="visit_date", value=datetime.date.today())

district_select = st.selectbox("SELECT DISTRICT:", [" ", "Bukomansimbi", "Butambala", "Gomba", "Kalungu", "Kyotera", "Lwengo", "Masaka City", "Mpigi", "Masaka Dist", "Kalangala", "Rakai", "Sembabule", "Wakiso",], key="district")

facility_select = st.selectbox("HEALTH FACILITY:", [" ", "Bigasa Health center III", "Butenga Health center III", "Kagoggo Health Centre II", "Kigangazzi Health Centre II",
"Kisojjo Health Centre II", "Kitanda Health Centre III", "Mirambi Health Centre III", "St. Mary's Maternity & Nursing Home", "Bulo Health Centre III", "Butaaka Health Centre III", "Epi-CentreSenge Health Ce[...]", 
"Kalamba Community Health Centre II", "Kibugga Health Centre II", "Kitimba Health Centre III", "Kiziiko Health Centre II", "Kyabadaza Health Centre III", "Ngando Health Centre III",
"Bulwadda Health Centre III", "Buyanja Health Centre II", "Kanoni Health Centre III", "Kifampa Health Centre III", "Kisozi Health Centre III", "Kitwe Health Centre II", "Kyayi Health Centre III", "Maddu Heal[...]", 
"Ngomanene Health Centre III", "Bubeke Health Centre III", "Bufumira Health Centre III", "Bukasa Health Centre IV", "Bwendero Health Centre III", "Jaana Health Centre II", "Kachanga Island Health Centre II",
"Mulabana Health Centre II", "Ssese Islands African Aids Project Health Centre II", "AHF Uganda Care", "Bukulula Health Centre IV", "Kabaale Health Centre III", "Kalungu Health Centre III", "Kasambya Health[...]", 
"MRC Kyamulibwa Health Centre II", "Nabutongwa Health Centre II", "Kabira Health Centre III", "Kabuwoko Govt Health Centre III", "Kakuuto Health Centre IV", "Kalisizo General Hospital", "Kasaali Health Cent[...]", 
"Mitukula Health Centre III", "Mutukula Health Centre III", "Nabigasa Health Centre III", "Ndolo Health Centre II", "Rakai Health Sciences Program Clinic", "Kakoma Health Centre III", "Katovu Health Centre [...]", 
"Kabayanda Health Centre II", "Kaliiro Health Centre III", "Kasagama Health Centre III", "Kinuuka Health Centre III", "Kyemamba Health Centre II", "Lyakajura Health Centre III", "Lyantonde General Hospital", 
"Masaka Municipal Clinic", "Masaka Police Health Centre III", "Mpugwe Health Centre III", "Nyendo Health Centre III", "TASO Masaka", "Bukakata Health Centre III",
"Bukeeri Health Centre III", "Buwunga Health Centre III", "Buyaga Health Centre II", "Kamulegu Health Centre III", "Kyanamukaaka Health Centre IV", "Bujuuko Health Centre III", "Bukasa Health Centre II", "Bu[...]", 
"Buwama Health Centre III", "Buyiga Health Centre III", "Dona Carnevale Medical Centre", "Fiduga Medical Centre", "Ggolo Health Centre III",
"Kampiringisa Health Centre III", "Kiringente Epi Health Centre II", "Kituntu Health Centre III", "Mpigi Health Centre IV", "Muduuma Health Centre III", "Nabyewanga Health Centre II", "Nindye Health Centre [...]", 
"Nsamu/Kyali Health Centre III", "Sekiwunga Health Centre III", "St. Elizabeth Kibanga Ihu Health Centre III", "Bugona Health Centre II",
"Butiti Health Centre II", "Buyamba Health Centre III", "Byakabanda Health Centre III", "Kacheera Health Centre III",
"Kasankala Health Centre II", "Kayonza Kacheera Health Centre II", "Kibaale Health Centre II", "Kibanda Health Centre III",
"Kibuuka Health Centre II", "Kifamba Health Centre III", "Kimuli Health Centre III", "Kyabigondo Health Centre II", "Kyalulangira Health Centre III",
"Lwabakooba Health Centre II", "Lwakalolo Health Centre II", "Lwamaggwa Govt Health Centre III", "Lwanda Health Centre III", "Lwembajjo Health Centre II",
"Magabi Health Centre II", "Rakai General Hospital", "Rakai Kiziba Health Centre III", "Busheka (Sembabule) Health Centre III",
"Kabundi Health Centre II", "Kayunga Health Centre II", "Kyabi Health Centre III", "Kyeera Health Centre III", "Lugusulu Health Centre III", "Lwebitakuli Gvt Health Centre IV",
"Lwemiyaga Health Centre III", "Makoole Health Centre II", "Mateete Health Centre III", "Mitima Health Centre II",
"Ntete Health Centre III", "Ntuusi Health Centre IV", "Sembabule Kabaale Health Centre II", "Ssembabule Health Centre IV",
"Bulondo Health Centre III", "Bunamwaya Health Centre II", "Busawamanze Health Centre III", "Bussi Health Centre III", "Buwambo Health Centre IV",
"Bweyogerere Health Centre III", "Community Health Plan Uganda", "Ggwatiro Nursing Home Hospital", "Gombe (Wakiso) Health Centre II",
"Joint Clinical Research Centre", "Kabubbu Health Centre IV", "Kajjansi Health Centre IV", "Kakiri Health Centre III",
"Kasangati Health Centre IV", "Kasanje Health Centre III", "Kasenge Health Centre II", "Kasoozo Health Centre III",
"Katabi Health Centre III", "Kawanda Health Centre III", "Kigungu Health Centre III", "Kimwanyi Health Centre II",
"Kira Health Centre IV", "Kireka Health Centre III", "Kirinya Health Centre III", "Kitala Health Centre II",
"Kiziba Health Centre III", "Kyengera Health Centre III", "Kyengeza Health Centre II", "Lubbe Health Centre II",
"Lufuka Valley Health Centre III", "Maganjo Health Centre II", "Magoggo Health Centre II", "Matuga Health Centre III",
"Mende Health Centre III", "Migadde Health Centre II", "Mildmay Uganda Hospital", "Mutundwe Health Centre II", "Mutungo Health Centre II",
"Nabutiti Health Centre III", "Nabweru Health Centre III", "Nakawuka Health Centre III", "Nakitokolo Namayumba Health Centre III",
"Nalugala Health Centre II", "Namayumba Epi Health Centre III", "Namayumba Health Centre IV", "Namugongo Fund for Special Children Clinic",
"Namulonge Health Centre III", "Nansana Health Centre II", "Nassolo Wamala Health Centre III", "Ndejje Health Centre IV",
"Nsaggu Health Centre II", "Nsangi Health Centre III", "Nurture Africa Clinic", "Seguku Health Centre II",
"TASO Entebbe", "Triam Medical Health Centre II", "Ttikalu Health Centre III", "Wagagai Health Centre IV",
"Wakiso Banda Health Centre II", "Wakiso EPI Health Centre III", "Wakiso Health Centre IV",
"Wakiso Kasozi Health Centre III", "Watubba Health Centre III", "Zzinga Health Centre III"], key="health_facility")

list_box = st.selectbox("Select Mentor/TA Provider:", [" ", "Denis", "Mercy", "Zipporah", "Eveline", "Lilian", "Ponsiano", "Dr Zikulah"], key="mentor")
additional_mentor = st.text_input("If other, specify name of Mentor/TA Provider:", key="additional_mentor")

text_input = st.text_input("Facility team members present during the visit (Names,Designations]:", key="facility_team")

purpose = st.text_input("Purpose of the Mentorship/Technical Assistance Visit:", key="purpose")
key_issues = st.text_area("Key Issues/gaps Identified During the Visit:", key="key_issues")
activities = st.text_area("Activities done to address the identified gaps:", key="activities")

action_plan = st.text_area("ACTION PLAN: Recommendations/Follow-up actions agreed upon with HF staff", key="action_plan")
followup_date = st.date_input("FOLLOW-UP DATE", format="DD/MM/YYYY", key="follow_up_date", value=datetime.date.today())

submit = st.button("SUBMIT REPORT")

if submit:
    # build data dictionary using the widget keys / variables
    data = {
        "VISIT DATE": st.session_state.get("visit_date"),
        "DISTRICT": st.session_state.get("district"),
        "HEALTH FACILITY": st.session_state.get("health_facility"),
        "MENTOR/TA PROVIDER": st.session_state.get("mentor"),
        "ADDITIONAL MENTOR/TA PROVIDER": st.session_state.get("additional_mentor"),
        "FACILITY TEAM MEMBERS PRESENT": st.session_state.get("facility_team"),
        "PURPOSE OF THE VISIT": st.session_state.get("purpose"),
        "KEY ISSUES/GAPS IDENTIFIED": st.session_state.get("key_issues"),
        "ACTIVITIES DONE TO ADDRESS GAPS": st.session_state.get("activities"),
        "ACTION PLAN": st.session_state.get("action_plan"),
        "FOLLOW-UP DATE": st.session_state.get("follow_up_date")
    }

    df = pd.DataFrame([data])
    table = pa.Table.from_pandas(df, preserve_index=False)

    out_dir = "emtct_reports.parquet"  # directory to store dataset partitions
    os.makedirs(out_dir, exist_ok=True)

    try:
        pq.write_to_dataset(
            table,
            root_path=out_dir,
            partition_cols=["DISTRICT", "HEALTH FACILITY"],
            existing_data_behavior="overwrite_or_ignore"
        )
        st.success("Report Submitted Successfully")
    except Exception as e:
        st.error(f"Failed to save report: {e}")

   # ...existing code...
    # Reset form fields to defaults so the form appears cleared after submit
    defaults = {
        "visit_date": datetime.date.today(),
        "district": "",
        "health_facility": "",
        "mentor": "",
        "additional_mentor": "",
        "facility_team": "",
        "purpose": "",
        "key_issues": "",
        "activities": "",
        "action_plan": "",
        "follow_up_date": datetime.date.today()
    }

    # Set keys individually and ignore any that Streamlit refuses to set
    for k, v in defaults.items():
            try:
                st.session_state[k] = v
        #except Exception:
            # skip keys that cannot be set during this run
            pass

    # optional: force a rerun to ensure widgets reflect the cleared state
    try:
        st.experimental_rerun()
    except Exception:
        pass
# ...existing code...
st.markdown("""---""")
       




















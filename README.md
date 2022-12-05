# Election_Analysis

## **Overview of Election Audit**

### **Purpose**

This was an audit of the tabulated results for a U.S. congressional precint in Colorado. It looked at the total votes cast, the total votes for each candidate, the percentage for each candidate, and the winner of the election. It also looked at the total votes per county and the county with the most votes cast.

## **Election-Audit Results**

![Shot of election results](https://github.com/Nacho567/Election_Analysis/blob/d4ab875a7348514460bd9249494d21489fc33a0b/shot_of_txt_results.png)

-**Total votes cast:** 369,711

-**County votes & percent of total votes:**
   - Jefferson: 10.5% (38,855)
   - Denver: 82.8% (306,055)
   - Arapahoe: 6.7% (24,801)
 
-**Largest county turnout: Denver**

-**Candidate votes & percent of total votes:**
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606)
 
-**Election winner:** Diana DeGette: 73.8% (272,892)

## **Election-Audit Summary:**

The script used for this audit could very easily be used for any other election audits with some modifications. The first modification would be to make sure the data input correctly lines up. The current script looks for a candidate and county in a certain block of the provided voting results. If the order of the data changes, certain results aren't needed (e.g. only candidate results and no county results), or only voting numbers are needed, the code can be changed to fit that. For example, it can be taken out or commented out ('#').

The second modification is simply changed the verbage for any input. If used on a country wide scale for example, the county lists and inputs could be changed to states, or the candidates could be changed to presidential candidates.

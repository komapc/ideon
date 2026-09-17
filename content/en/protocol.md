---
title: Protocol
---

# Counting protocol

Every figure on the [examples](examples.html) page is a Fermi estimate made before the rules were written down. Here it is the other way round: the rules come first, and the example is computed under them afterwards. The order is fixed in the repository history: the commit with the rules precedes the commit with the calculation. [Page history on GitHub](https://github.com/komapc/ideon/commits/main/content/en/protocol.md).

## 1. Rules

Written before the calculation and not changed after it. If a rule turned out badly, that is recorded as a result of the test, and the number is not fitted.

**R1. Inputs.** Only external, checkable quantities: documents, statistics, publications. Every number with a reference. The site author's own estimate is not an input.

**R2. What is counted.** One channel of emission, declared in advance. Side channels, such as fame, stories about the person and people inspired by them, are not counted unless declared before the calculation.

**R3. Minutes M.** A saved life is the whole remaining life of the person saved; for a newborn, 1 Vt = 2.5 × 10⁷ minutes. A text read is reading time × number of readers. A speech heard is duration × listeners.

**R4. Horizon.** The account runs from the start of emission to the moment of calculation. The future is not counted, except for lives already begun: those are counted to their end.

**R5. Degree G.** Fixed categories; the nearest one is chosen, interpolation is forbidden.

| Category | G |
|---|---|
| Life instead of death | 1 |
| Severe disability prevented | 0.5 |
| Frame, conversion: changed what one lives by | 0.5 |
| Knowledge or skill where other sources exist | 0.2 |
| Opinion | 0.05 |
| Attention without shift | 0.01 |

**R6. Share.** List every link in the chain without which the result would have been different. For each link, two numbers: p, the probability the result would have happened without it; d, the fraction of the horizon lost to delay if it had. Raw weight w = (1 − p) + p × d. Share of a link = w / Σw. This is a chain approximation of the Shapley value: reproducible and efficient.

**R7. Sign S.** By result. Search for documented harm from the same channel: lawsuits, product recalls, medical complications, recognized victims. If found, S = (benefit − harm) / (benefit + harm) in minutes. If the search was done and found nothing, S = +1, stating where the search was made. S = +1 is not assigned without a search.

**R8. Coherence Q.** The fraction of emissions whose sign by intention matched the sign by result. For one channel with one documented intention: 1 if they matched, 0 if not.

**R9. Error.** Every input is an interval. The result is computed at the extreme values and reported as an interval and an order of magnitude. No point figure is reported.

**R10. Judgment points.** Every place where a rule does not determine the number uniquely is marked ◆ and given an interval with an explanation. Their count is also a result of the test.

**R11. No fitting.** After the result is obtained, rules, categories and intervals are not changed. A discrepancy with previously published figures is recorded, not removed.

## 2. Declared example

**James Harrison** (1936–2025), Australian donor of plasma with anti-D antibodies. Chosen because he has exactly one channel of emission, a deed, and the inputs exist in documents: the number of donations, the number of doses, the epidemiology of Rh disease.

By R2 only the plasma channel is counted. His fame, and donors who came because of his story, are not counted: that is a second channel, and its rules are not declared here.

Inputs to be found before the calculation:

1. Number of donations and years.
2. Number of anti-D doses made with his plasma, and the year the program began.
3. Number of births in Australia during the program.
4. Mortality from hemolytic disease of the newborn before and after prophylaxis.
5. The share of the fall in mortality attributable to anti-D rather than to intrauterine transfusion and neonatal care.
6. Size of the anti-D donor pool in Australia.
7. History of the discovery of anti-D: how many independent groups.
8. Documented harm from anti-D.

## 3. Inputs

| # | Quantity | Value | Source |
|---|---|---|---|
| 1 | Donations | 1,173 over 1954–2018; in the anti-D program from 1967 to 2018, 51 years | Lifeblood |
| 2 | Doses containing his plasma | "more than 3 million" since 1967; the press says "2.4 million babies" | Lifeblood, CBS |
| 3 | Births in Australia 1967–2024 | 15.3 million (58 years, 264 thousand a year on average; 292,318 in 2024) | ABS; yearly series via Wikipedia |
| 4 | Mortality from hemolytic disease of the newborn | 46 per 100,000 births before prophylaxis, 1.6 after | GLOWM |
| 5 | Share of the fall attributable to anti-D | sensitization fell 80–90%; mortality also fell with Doppler (1970s), intrauterine transfusion (1980s), neonatal care | BioDrugs, PMC |
| 6 | Anti-D donor pool in Australia | under 200, 100–150 active | ABC, Lifeblood |
| 7 | Discovery of anti-D | two independent groups: Liverpool (Finn, Clarke, 1960–64) and New York (Freda, Gorman, Pollack, 1963); Lasker Award 1980 to four | Lasker, Wikipedia |
| 8 | Documented harm | hepatitis C transmitted by anti-D: Ireland 1977–78 (704 infected, 18 dead by 2017), East Germany 1978–79 (several thousand). No cases found in the Australian channel | NEJM, PubMed |

Input 2 does not enter the calculation: a dose is not a life. It is listed because the earlier estimate grew out of it.

## 4. Calculation

**Minutes (R3, R4).** Deaths averted by the whole Australian program over 58 years: 15.3 × 10⁶ × (46 − 1.6) / 10⁵ = 6,800, of which a fraction f is attributable to anti-D.

◆ f = 0.5–0.9. Sensitization fell 80–90%, but part of the fall in mortality came from transfusion and neonatal care. The 46 → 1.6 series is British; carrying it over to Australia is also a judgment, the Rh distribution of the populations being similar.

Deaths averted: 3,400–6,100. Severe disability averted (kernicterus in survivors) ◆ 0.5–1 per death, R5 category "disability", G = 0.5. Life-equivalents: 4,250–9,150. Each is a newborn and by R4 counts to the end: 1 Vt.

Impact of the whole program: (4.3–9.2) × 10³ Vt, that is (1–2) × 10¹¹ ideons.

**Share (R6).** Links in the chain from discovery to the dose in the midwife's hand:

| Link | p: would have happened without it | d: horizon lost | w = (1 − p) + p·d |
|---|---|---|---|
| Discovery, two groups | ◆ 0.8–0.9 (found independently twice in three years) | ◆ 0.09–0.26 (5–15 years of 58) | 0.18–0.41 |
| National program, fractionation | ◆ 0.7–0.9 (imports) | ◆ 0.05–0.2 | 0.15–0.44 |
| Donor pool without Harrison | ◆ 0.5–0.8 (imports) | ◆ 0.1–0.3 | 0.28–0.65 |
| Clinicians | 0.99 | 0 | 0.01 |
| Harrison | 1 − s·r | 0 | s·r = 0.0004–0.05 |

For Harrison, p splits into two numbers. ◆ s is his share of the pool's antibody: one of 100–200 donors, but 51 years and a high titre; 1–5%. ◆ r is the fraction of his supply the program could not have replaced: if donors can be immunized to order, the shortfall closes within a couple of years out of 51, r ≈ 0.04; if supply is scarce (Australia imports immunoglobulins, the pool is small), every donation is marginal, r = 1. Interval r = 0.04–1.

Harrison's share = w / Σw: from 0.0004 / 1.51 to 0.05 / 0.67, that is **0.03–7%**.

**Result.** I = (1–2) × 10¹¹ × (0.0003–0.075) = 3 × 10⁷ – 2 × 10¹⁰ ideons:

> **I(Harrison) = 1–700 Vt**, order of magnitude 10¹ Vt.

**Sign (R7).** A web search was made for adverse events and contamination via anti-D. It surfaced the Irish and East German hepatitis C outbreaks, each from a single infected donor (NEJM, PubMed); both are other pools, other countries. No Australian case surfaced; Lifeblood and National Blood Authority reports were not read for harm. **S = +1.**

**Coherence (R8).** The intention is documented: after transfusions at fourteen he pledged to become a donor, and donation was his only channel. The sign of intention and the sign of result matched. **Q = 1.**

**Judgment points: ten.** Carrying the British mortality series over to Australia is not marked separately: it is folded into the interval of f.

## 5. What the test showed

**The earlier figure was wrong by one to four orders of magnitude.** The examples page gave Harrison 5–30 kVt. Under the rules he gets 1–700 Vt. Two errors: "2.4 million" is doses and mothers, not babies saved; the whole program saved thousands, not hundreds of thousands. And the 3–6% share was taken by plasma volume, not by replaceability: the donor pool is replenished by immunizing volunteers, and without any one donor most doses would still exist.

**The interval spans three orders of magnitude, and half of it is one number.** Of ten judgment points, r, the replaceability of a donor in a replenishable pool, contributes a factor of 25 on its own; the other nine together contribute about 25 more, the largest of them, s, his share of the pool's antibody, being 5. This is exactly the warning on the [mathematics](math.html) page: v(S) is not measured but estimated. The rules are reproducible: a second person with the same inputs gets the same interval. Not the same number.

**What holds.** Even at the lower bound Harrison is above the typical person (0.4 Vt); even at the upper bound he is two orders of magnitude below Trump (40 kVt). The whole Australian anti-D program is (4–9) × 10³ Vt, ten thousand biographies. The ordering between rows of the tables holds, the absolute figures do not, as the front page promises.

**Which rules worked and which did not.** R5 with fixed categories worked: no dispute about the degree arose. R7 worked unexpectedly: without the mandatory search for harm the sign would have been assigned automatically, and the product does have harm on record, if in other countries. R6 fell short: the rule does not say how to count the replaceability of one member of a replenishable pool, and that produced the widest interval. A rule is needed, but by R11 it is not added here.

**The other tables on the site have not been re-run under these rules.** Harrison's row on the examples page has been corrected with a link here; the other rows are the earlier Fermi estimates, and after this test they should be read as orders of magnitude, not figures.

## 6. Sources

- Australian Red Cross Lifeblood, [James Harrison's story](https://www.lifeblood.com.au/news-and-stories/stories/james-harrison): 1,173 donations, more than 3 million doses since 1967.
- CBS News, [James Harrison, credited with saving 2.4 million babies, dies at 88](https://www.cbsnews.com/news/james-harrison-blood-plasma-donations-2-4-million-babies-dead-88/).
- Australian Bureau of Statistics, [Births, Australia, 2024](https://www.abs.gov.au/statistics/people/population/births-australia/latest-release); yearly series 1967–2024 via [Demographics of Australia](https://en.wikipedia.org/wiki/Demographics_of_Australia).
- GLOWM, [Anti-RhD immunoglobulin for the prevention of HDFN](https://www.glowm.com/article/heading/vol-16--the-prevention-and-management-of-rh-disease--antirhd-immunoglobulin-for-the-prevention-of-hemolytic-disease-of-the-fetus-and-newborn-polyclonal-versus-monoclonal-antibodies/id/418843): mortality 46 → 1.6 per 100,000 births.
- PMC, [Forty years of anti-D immunoprophylaxis](https://ncbi.nlm.nih.gov/pmc/articles/PMC2535875); BioDrugs, [The role of immunoglobulins in neonatal Rhesus haemolytic disease](https://link.springer.com/article/10.2165/00063030-200115080-00005): contribution of prophylaxis and of other methods.
- ABC News, [There are only 100 anti-D plasma donors in Australia](https://amp.abc.net.au/article/101564234); Lifeblood, [Pregnancy, anti-D and plasma](https://www.lifeblood.com.au/donors/blood-plasma-platelets/learn/plasma/anti-D).
- Lasker Foundation, [Vaccine for preventing Rh incompatibility in newborns](https://laskerfoundation.org/winners/vaccine-for-preventing-rh-incompatibility-in-newborns/); [Ronald Finn](https://en.wikipedia.org/wiki/Ronald_Finn).
- NEJM, [Clinical outcomes after hepatitis C infection from contaminated anti-D immune globulin](https://www.nejm.org/doi/full/10.1056/NEJM199904223401602); PubMed, [Contaminated anti-D immunoglobulin in the GDR](https://pubmed.ncbi.nlm.nih.gov/32050283/).
- ABC News, [Australia's reliance on imported blood plasma](https://www.abc.net.au/news/2024-07-07/donating-blood-plasma-money-red-cross-supply/103923554): immunoglobulin imports.

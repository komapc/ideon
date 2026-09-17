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

The calculation is in the next commit.

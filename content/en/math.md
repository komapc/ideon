---
title: Mathematics
description: The core of ideonology in testable form: the minute as a partition, three axioms, four rules of transmission, one conservation law, the Shapley value, R₀ and parity.
---

# Mathematics

This page collects the core of the theory in a form that can be tested and argued with: one primitive, three axioms, four rules of transmission, one conservation law. Notation is in the [glossary](glossary.html).

## 1. The minute and its division

The primitive of the theory is one minute of one person's thought. Every minute has sources: those without whom it would have been different. There are three kinds of source: other people, the person themself, and the non-human world. The minute is divided among them completely:

> Σ<sub>A</sub> w<sub>A</sub>(m) + s(m) + n(m) = 1

where w<sub>A</sub>(m) ≥ 0 is the part of minute m that belongs to another person A; s(m) is selfhood, the part the person made themself; n(m) is nature, the part shaped by what is not human: the minute you spend looking at a tree.

The impact of a person A is the sum of A's parts in all other people's minutes:

> I(A) = Σ<sub>other people's minutes m</sub> w<sub>A</sub>(m)

The unit of measurement is the peirce (Ps): one minute of someone else's, wholly yours. Your own minutes do not enter your impact: selfhood is a source, not an account.

**Three axioms.**

- **A1. Equality of minutes.** Everyone has sixty minutes an hour, and a child's minute weighs the same as an academician's.
- **A2. Completeness.** Every minute is divided among its sources without remainder; the parts are non-negative and add up to one.
- **A3. Irreplaceability.** A source's part equals what would disappear without it. What would have happened anyway stays with the minute's previous owners.

**What counts as an ideon.** Anything by which one person got into someone else's minute: an idea, a book, a theory, a language, a habit, an institution, a deed nobody recognized as an idea. These are channels, not summands: the sum runs over minutes, and the boundary between ideons does not affect it. Euclid's geometry can be treated as one ideon or as the 465 propositions of the Elements; the number of peirces comes out the same. Four borderline cases:

- A reader of an article avoided a mistake in a decision. What counts is the minutes of the decision and of its consequences that came out different from the world without the article; the degree is how different.
- A reader merely saw a corrected figure. If their later minutes did not change, the degree is zero: no ideon occurred.
- The figure was then used by the next person. That is re-emission, a new link in the chain; the share is split between the author of the figure, the editor and the reteller.
- The author of the figure is unknown. Their share is credited to the Anonymous; the shares of the others do not grow because of it.

An ideon has to be tracked as a thing only in section 7, for R₀ and the Lindy effect. Any trackable thing will do there — a word, a theorem, a custom; the slicing is a working convention.

## 2. Degree: how much of the minute is captured

The degree of an ideon, G ∈ [0, 1], is the part of the minute it captured. The rest stays with those who shaped the minute before. It is not a separate multiplier on top of the division but the size of the piece that gets divided further. The degrees of all the ideons that landed in one minute add up to no more than one: there is only one minute.

Degree is measured as an angle. Let T₁ be a person's behavioral trajectory after meeting the ideon (what they say and do), and T₀ the counterfactual trajectory without it. Then

> G = ∠(T₁, T₀) / 180°

0°: nothing changed. 90°: a new topic; the person is thinking about something they otherwise never would have. 180°: a reversal. Behavior space is not Euclidean, and "angle" here is a name for the distance between two distributions of future words and deeds, with the ideon and without it.

Practical estimates of G, in increasing order of precision: a survey ("would you have thought about this otherwise?"); a behavioral test (A/B, a randomized trial); a predictive test (how many bits better a person's subsequent words and actions can be predicted if one knows about the ideon); embeddings of texts before and after, where the cosine gives the angle directly.

The degree depends not only on content but on the trust between emitter and receiver: G = content × receptivity. The same thing from a friend and from a stranger shifts differently.

## 3. Share: the Shapley value

The captured part of the minute is divided among everyone party to it: the author, the author's teacher, the reteller, the publisher. If the participants are N = {1, …, n}, the share of participant A equals A's average marginal contribution over all orders of joining:

> w<sub>A</sub> = Σ<sub>S ⊆ N∖{A}</sub> |S|! (n − |S| − 1)! / n! × [v(S ∪ {A}) − v(S)]

where v(S) is the part of the minute that would have been the same through the efforts of coalition S alone. The world without A is not a single world: without A the result might not have happened, might have happened later, or through someone else. So v(S) is not a quantity in one imagined world but the expectation over the distribution of such worlds, and A's share is the expected loss from removing A. This is the only division rule satisfying four axioms: efficiency (shares add up to the whole), symmetry (equal contribution, equal share), zero for zero contribution, and additivity. Axiom A3 is exactly this rule; efficiency gives the completeness of A2 within the captured part.

The intuition: your share equals what would disappear if you were removed. Hence irreplaceability as the main multiplier. A reteller can be replaced by another reteller; the author cannot. The doctor on call can be replaced; the only paramedic cannot. Mitochondrial Eve is replaceable: had she died childless, someone else would have been Eve, and the minutes would have remained the same. For history, v(S) cannot be measured directly: the shares in the tables are estimated by a single counterfactual question, whether the same would have happened without this person and how much later, and after degrees this is the largest source of error.

The practical recipe in all the tables of this site is one:

> I ≈ reach × degree × share

This is not a product of three independent quantities but two successive divisions of one minute: first the ideon separates its part, then that part is divided along the chain. A first approximation for long chains: minutes (reach) go to the deliverer, the reteller, publisher, translator; degrees (depth) go to the author. A reteller who improves the idea takes a portion of the degrees.

## 4. Four rules of transmission

**Capture.** An ideon takes a part G of the minute; the rest stays with the previous owners. To get into someone else's minute you have to displace someone from it: an earlier ideon, the Anonymous, nature, or the person themself.

**Chain.** The captured part is divided among the links of the chain by irreplaceability. Re-emission adds a link and a share for it, but creates no new impact in the same minute: the same part is being divided. New impact arises only in new minutes that the ideon has reached.

**Cargo.** Each transmission copies only what the ideon cannot work without. A name is almost never part of the working load and is the first thing lost. If the probability of losing the name in one transmission is p, after k transmissions it survives with probability (1 − p)<sup>k</sup>; the content survives because it is what people copy for. Hence the Anonymous: not a separate player but the sum of the accounts whose owners are unknown. The exception proves the rule: when the name is part of the working load ("as Einstein said"), it not only survives but sticks to other people's words.

**Dissipation.** An ideon is a flow, not a stock. Without re-emission the capture of new minutes tends to zero: forgetting, distraction, death. The natural state of an ideon is to be forgotten; posthumous impact is possible only through the chain. The condition for survival is in section 7.

**Damping is a consequence, not a rule.** The chain of causes is infinite backwards, but the sum of shares converges on its own: one minute is being divided, and there is no more than one to divide. A distant link gets less because the further back it is, the more likely the result would have come about without it: truth is rediscovered, a reteller can be replaced. Damping follows irreplaceability, not distance: a distant author can weigh more than a nearby reteller. The rate of damping is the theory's only value-laden parameter, and it lives in how generously v(S) grants "it would have happened anyway": generously, and damping is fast and the world is one of deeds; stingily, and damping is slow and the world is one of culture. The question "who matters more, the doctor or Plato" is a question about one coefficient.

The vertical chain (parents, ancestors) is cut off by irreplaceability itself: parents are credited not for the child's existence but for raising it, that is, for degrees, and within two or three generations an ancestor's share becomes indistinguishable from zero.

## 5. The conservation law

There is one law, and it follows from A1 and A2:

> Σ<sub>A</sub> I(A) = Σ<sub>B</sub> incoming account(B)

**As much as everyone has given, everyone has received.** A person's incoming account is everything in their minutes that was shaped by other people: their life minus selfhood and nature. The sum runs over all people and all times, including minutes not yet lived.

This is conservation of attribution, not a law of nature: a bookkeeping identity that keeps the theory from creating impact out of thin air or losing it. It works the way conservation laws work in physics: it forbids.

- **Attention is a zero-sum game.** There are sixty minutes an hour per person, and each already belongs to someone. A new ideon enters a minute only by displacement.
- **Bookkeeping does not create credit.** A share in a minute can be gained only at the expense of another of its sources.
- **The speed limit.** In one hour no more minutes can be given away than humanity lived in that hour.

**Where the new comes from.** If everyone's selfhood were zero, the ledger would be closed: every ideon would turn out to be a retelling of the Anonymous, and nothing new would ever enter it. Selfhood is the wellspring: a new ideon is born in one's own part of the minute, and becomes impact only when it reaches someone else's head.

**Not conserved:** sign (can change posthumously when an idea is put to different use; Christian grace zeroes it from outside); coherence (no budget and no rivalry; everyone raises their own toward one without taking from anyone).

There is one symmetry behind the law: the equality of heads. Sign has no symmetry, which is why it is not conserved: the arbiter sets it.

## 6. Three axes of one vector

A person's full assessment is not a number but a triple:

> (I, S, Q)

I is magnitude, S ∈ [−1, 1] is sign, Q ∈ [0, 1] is coherence, defined as the correlation between sign-by-intention and sign-by-result over all of a person's emissions. If a single figure is needed, I × S × Q, where Q is a multiplier on the sign, not a value in its own right: a coherent villain is more dangerous than a chaotic one.

The three numbers are conveniently read as one vector. An ideon has a length, its degree, the captured part of the minute, and a direction: where the thought moved. Sign is the cosine of the angle between that direction and the axis of "better" set by the arbiter; that is why S lies between −1 and 1, and why one ideon has different signs under different arbiters. Coherence is how far the direction aimed at matched the direction actually shifted; the correlation of signs is its shadow on the arbiter's axis, the only thing observable. The vector itself need not be known: a length and two projections are enough.

Bookkeeping adds lengths, while the shift of a person is the vector sum. Propaganda and counter-propaganda both occupied their minutes and both earned impact, but the net shift is about zero.

At high Q, intention and result coincide, and either can be used for the count. At low Q, intention predicts nothing. Thus Q dissolves the classic dispute "intention or consequences": it says for whom that dispute even makes sense.

## 7. Dynamics: R₀ and Lindy

An ideon survives if the rate of re-emission is not below the rate of forgetting. Let R₀ be the average number of new carriers produced by one carrier. Then

> R₀ > 1: the chain sustains itself; R₀ < 1: it dies out.

Fame raises the chance of being retold, so above a certain mass the chain accelerates itself, and below it stalls on its own. A threshold, not a smooth scale.

Rate of dissipation = (frequency of occasion) × (probability of transmission on each occasion). The first factor depends on how the ideon is attached to recurring situations; the second on the cost of copying, emotional charge, detachability from context, and the presence of an institutional carrier that re-emits on schedule.

The age distribution of ideons is not exponential but power-law: the longer an ideon has lived, the longer it has left (the Lindy effect). Survival is selection for the properties listed.

## 8. Units

> 1 Vt ≡ 2.5 × 10⁷ Ps

This is all the waking thought of one person over a lifetime: about 350,000 minutes per year for 70 years. The coefficient is fixed by definition, like the speed of light. The symbol is Vt, because V is taken by the volt.

| Subunit | Peirces | Scale |
|---|---|---|
| 1 µVt | 25 | one conversation |
| 1 mVt | 25,000 | one deed |
| 1 Vt | 2.5 × 10⁷ | one biography, parity |
| 1 kVt | 2.5 × 10¹⁰ | a politician, a celebrity |
| 1 MVt | 2.5 × 10¹³ | a founder of a religion |
| 1 GVt | 2.5 × 10¹⁶ | the Anonymous |

Humanity's entire budget over all of history: about 117 billion people, but the average life lived is much shorter than a Vita; roughly half died as children. That comes to the order of 10¹⁸ minutes, or 40 GVt. By the conservation law the sum of all impacts in history is no greater than this number: it equals it minus selfhood and nature.

## 9. The incoming account and parity

Every person has an incoming account: who shaped their minutes. It equals the life lived minus selfhood and nature, and it is different for everyone. To the accuracy at which the theory counts, for a full life it is one Vita. Parity is repayment of the debt: you gave no less than you received. The working threshold:

> I(A) ≥ 1 Vt

The typical person accumulates about 0.4 Vt by death, and most never reach the threshold. The mean outgoing account nonetheless equals the mean incoming one, identically, by the conservation law. The gap between median and mean is the heavy tail: the Anonymous and the founders of religions hold what the majority fell short of.

## 10. Symmetry of channels

A channel is symmetric if its participants give and receive equally. Let a conversation have n people, let participant i speak a fraction f<sub>i</sub> of the time (one person speaks in any given minute, Σ f<sub>i</sub> = 1), let it last T minutes, and let every remark have the same degree G. Then the participant gave f<sub>i</sub> × T × (n − 1) × G, received (1 − f<sub>i</sub>) × T × G, and

> balance = T × G × (n × f<sub>i</sub> − 1)

- For two people with equal time the balance is zero: a conversation is a symmetric channel, and both earn impact at the expense of the previous owners of those minutes.
- For three, whoever speaks more than a third of the time gives more than they receive. The symmetry of a channel is the equality of speaking time; no separate quantity is needed for it.
- A lecture is the same case with n = 101 and f = 1: the balance is 100 × T × G. The lecturer's leverage is in the number of listeners, not in depth: a routine lecture has a degree close to zero, and then a hundred listeners add nothing.
- A silent third person also gets a share if the other two speak differently in their presence than they would without them: by A3, those minutes would have been different without that person.
- One conversation will not get you to parity: a symmetric channel has a leverage of one. Leverage in the tens of thousands comes not from the number of listeners but from asynchrony (a book, a recording, an institution), and the main asymmetry of the whole ledger is time: we receive from the past and give to the future.

## 11. Limits of applicability

The theory is mind-centric: a deed that touched no head weighs zero. But touching runs along the causal chain, not through renown: a planted forest counts through the minutes it changed, shade, harvest, a village spared a drought, even if no one ever thought about the forest itself, just as a saved infant is credited to a donor it will never know of. A forest that touched no life weighs zero. Animal minutes are not counted for now; that is a separate decision. Selfhood and nature enter the division of the minute but are not measured: the theory counts only what passed from head to head. The theory systematically underrates art, because art shifts perception rather than behavior, and the angle catches that only indirectly. The scale of degrees is the main source of error in all estimates: the ordering between rows of the tables is robust, the absolute figures are good to one or two orders of magnitude.

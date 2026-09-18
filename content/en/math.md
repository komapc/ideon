---
title: Mathematics
---

# Mathematics

This page collects the definitions and laws in a form that can be tested and argued with. Notation is in the [glossary](glossary.html).

## 1. The basic quantity

The impact of a person A is the sum over all minutes of other people's thought that A was party to:

> I(A) = Σ<sub>minutes m</sub> G(m) × w<sub>A</sub>(m)

where G(m) ∈ [0, 1] is the degree of shift of minute m, and w<sub>A</sub>(m) is A's share of that minute. The unit of measurement is the peirce (Ps): one minute at G = 1 and w = 1.

**What counts as an ideon.** Anything that shifted someone else's minute: an idea, a book, a theory, a language, a habit, an institution, a deed nobody recognized as an idea. These are channels, not summands: the sum runs over minutes, and the boundary between ideons does not affect it. Euclid's geometry can be treated as one ideon or as the 465 propositions of the Elements; the number of peirces comes out the same. Four borderline cases:

- A reader of an article avoided a mistake in a decision. What counts is the minutes of the decision and of its consequences that came out different from the world without the article; the degree is how different.
- A reader merely saw a corrected figure. If their later minutes did not change, the degree is zero: no ideon occurred.
- The figure was then used by the next person. That is re-emission, a new link in the chain; the share is split between the author of the figure, the editor and the reteller.
- The author of the figure is unknown. Their share is credited to the Anonymous; the shares of the others do not grow because of it.

An ideon has to be tracked as a thing only in section 7, for R₀ and the Lindy effect. Any trackable thing will do there — a word, a theorem, a custom; the slicing is a working convention.

I is dimensionless with respect to "person": a child's minute and an academician's minute weigh the same. This is an egalitarian axiom, the equality of heads, and the zeroth law, the budget of minutes, follows from it. The first law follows from a different axiom: Shapley efficiency.

## 2. Degree as an angle

Let T₁ be a person's behavioral trajectory after meeting the ideon (what they say and do), and T₀ the counterfactual trajectory without it. Then

> G = ∠(T₁, T₀) / 180°

0°: nothing changed. 90°: a new topic; the person is thinking about something they otherwise never would have. 180°: a reversal. The ceiling of 180° arises on its own, and it sets the third law. Behavior space is not Euclidean, and "angle" here is a name for the distance between two distributions of future words and deeds, with the ideon and without it.

Practical estimates of G, in increasing order of precision: a survey ("would you have thought about this otherwise?"); a behavioral test (A/B, a randomized trial); a predictive test (how many bits better a person's subsequent words and actions can be predicted if one knows about the ideon); embeddings of texts before and after, where the cosine gives the angle directly.

The degree depends not only on content but on the trust between emitter and receiver: G = content × receptivity. The same thing from a friend and from a stranger shifts differently.

## 3. Share: the Shapley value

If the participants in minute m are N = {1, …, n}, the share of participant A equals A's average marginal contribution over all orders of joining:

> w<sub>A</sub> = Σ<sub>S ⊆ N∖{A}</sub> |S|! (n − |S| − 1)! / n! × [v(S ∪ {A}) − v(S)]

where v(S) is the degree that would have resulted from the efforts of coalition S alone. The world without A is not a single world: without A the result might not have happened, might have happened later, or through someone else. So v(S) is not the degree in one imagined world but the expectation over the distribution of such worlds, and A's share is the expected loss from removing A. This is the only division rule satisfying four axioms: efficiency (shares add up to the whole), symmetry (equal contribution, equal share), zero for zero contribution, and additivity.

The intuition: your share equals what would disappear if you were removed. Hence irreplaceability as the main multiplier. A reteller can be replaced by another reteller; the author cannot. The doctor on call can be replaced; the only paramedic cannot. Mitochondrial Eve is replaceable: had she died childless, someone else would have been Eve, and by the zeroth law the minutes would have remained the same. For history, v(S) cannot be measured directly: the shares in the tables are estimated by a single counterfactual question, whether the same would have happened without this person and how much later, and after degrees this is the largest source of error.

A first approximation for long chains: minutes (reach) go to the deliverer, the reteller, publisher, translator; degrees (depth) go to the author. A reteller who improves the idea takes a portion of the degrees.

## 4. Damping

The chain of causes is infinite backwards. Without damping the sum of shares diverges and all impact drains to the Big Bang. What is required is that

> Σ<sub>along the chain</sub> w = c < ∞

The constant c is the same for everyone, so comparisons between people do not depend on it. The role is the same as that of the damping factor in PageRank: the sum has to converge. The mechanism is different. PageRank damps by distance, at every hop; here it is the Shapley shares themselves that decline, because the further back a link is, the more likely the result would have come about without it: truth is rediscovered, a reteller can be replaced. There is no separate multiplier on top of the shares; otherwise a distant author would be penalized twice. That is why damping follows irreplaceability, not distance: a distant author can weigh more than a nearby reteller. The rate of damping is the theory's only value-laden parameter, and it lives in how generously v(S) grants "it would have happened anyway": generously, and damping is fast and the world is one of deeds; stingily, and damping is slow and the world is one of culture. The question "who matters more, the doctor or Plato" is a question about one coefficient.

The vertical chain (parents, ancestors) is cut off by irreplaceability itself: parents are credited not for the child's existence but for raising it, that is, for degrees, and within two or three generations an ancestor's share becomes indistinguishable from zero.

## 5. Conservation laws

**Zeroth law: the budget of minutes.** Total thought per unit of time is fixed:

> Σ M = N × 60 min/hour

where N is the population. Every minute is spent on something. This is the only strictly conserved quantity. Consequence: attention is a zero-sum game.

**First law: conservation of credit.** Bookkeeping does not create impact:

> Σ<sub>A</sub> I(A) = c × Σ<sub>m</sub> G(m)

This is the Shapley efficiency axiom. Credit can be gained only at the expense of another participant in the same chain receiving less.

**Second law: dissipation.** An ideon is a flow, not a stock. Any shift without re-emission tends to zero: forgetting, distraction, death. The natural state of an ideon is to be forgotten. Posthumous impact is possible only through the chain.

**Third law: the speed limit.** Since G ≤ 1, humanity's maximum impact per unit of time is bounded:

> dI/dt ≤ N × 60 × c

A bound, not a conservation law: the analogue of the speed of light.

**Not conserved:** degrees (created and dissipated, no budget); sign (can change posthumously when an idea is put to different use; Christian grace zeroes it from outside); coherence (no budget and no rivalry; everyone raises their own toward one without taking from anyone).

By Noether, each law corresponds to a symmetry. Minutes are conserved because all heads are equal. Credit is conserved because of the Shapley efficiency axiom. Sign is not conserved because it has no symmetry: the arbiter sets it.

## 6. Three axes

A person's full assessment is not a number but a triple:

> (I, S, Q)

I is magnitude, S ∈ [−1, 1] is sign, Q ∈ [0, 1] is coherence, defined as the correlation between sign-by-intention and sign-by-result over all of a person's emissions. If a single figure is needed, I × S × Q, where Q is a multiplier on the sign, not a value in its own right: a coherent villain is more dangerous than a chaotic one.

At high Q, intention and result coincide, and either can be used for the count. At low Q, intention predicts nothing. Thus Q dissolves the classic dispute "intention or consequences": it says for whom that dispute even makes sense.

## 7. Dynamics: R₀ and Lindy

An ideon survives if the rate of re-emission is not below the rate of forgetting. Let R₀ be the average number of new carriers produced by one carrier. Then

> R₀ > 1: the chain sustains itself; R₀ < 1: it dies out.

Fame raises the chance of being retold, so above a certain mass the chain accelerates itself, and below it stalls on its own. A threshold, not a smooth scale.

Rate of decay = (frequency of occasion) × (probability of transmission on each occasion). The first factor depends on how the ideon is attached to recurring situations; the second on the cost of copying, emotional charge, detachability from context, and the presence of an institutional carrier that re-emits on schedule.

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

Humanity's entire budget over all of history: about 117 billion people times 25 million minutes, on the order of 10¹⁸ peirces, or 40 GVt. Check: the typical person accumulates about 10⁷, and the mean over everyone, with the tail of the Anonymous and the founders, about 2.5 × 10⁷; multiply by 117 billion and you get on the order of 10¹⁸ again. The constant c is about one, and the first law is not violated.

## 9. The incoming account and parity

Every person has an incoming account: who shaped their minutes. By the first law it equals exactly one Vita. Parity is the condition

> I(A) ≥ 1 Vt

that is, repayment of the debt. The typical person accumulates about 0.4 Vt by death, and most never reach the threshold. The arithmetic mean is nonetheless exactly 1 Vt: the first law requires it at c = 1. The gap between median and mean is the heavy tail: the Anonymous and the founders of religions hold what the majority fell short of.

## 10. Limits of applicability

The theory is mind-centric: a deed that touched no head weighs zero. But touching runs along the causal chain, not through renown: a planted forest counts through the minutes it changed, shade, harvest, a village spared a drought, even if no one ever thought about the forest itself, just as a saved infant is credited to a donor it will never know of. A forest that touched no life weighs zero. Animal minutes are not counted for now; that is a separate decision. The theory systematically underrates art, because art shifts perception rather than behavior, and the angle catches that only indirectly. The scale of degrees is the main source of error in all estimates: the ordering between rows of the tables is robust, the absolute figures are good to one or two orders of magnitude.

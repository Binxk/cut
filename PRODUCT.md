# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
[Inferred from brief] Psychology researchers, students, and evidence-curious readers. Primary user: a psych researcher (the product owner is one) scoping a literature question — "what studies exist linking variable X and variable Y, and how strong is the design behind them?" Used at a desk, during literature review or study planning.

## Product Purpose
A free, no-login search tool over PubMed's psychology literature. The user enters variables of interest (e.g., "sleep", "stimulant use") and optionally a study-design type (meta-analysis, RCT, observational…); the tool returns matching papers with abstracts, detected study design, and the variables highlighted in context. Success: the user can answer "what's the evidence and what kind of evidence is it?" in minutes without knowing PubMed query syntax.

## Positioning
Unlike PubMed's own UI, design filters and variable terms are first-class, side-by-side inputs — no field-tag syntax needed. Unlike Elicit/Consensus, it is free, quota-less, and psych-scoped. It runs entirely in the browser against the public NCBI E-utilities API: no server, no account, no cost.

## Operating Context
Literature reviews, study planning, meta-analysis scoping. The user thinks in psych-methods vocabulary: IV/DV, observational vs. experimental, cross-sectional vs. longitudinal, effect sizes, N. Sits alongside PubMed (results deep-link to it), reference managers, and spreadsheets.

## Capabilities and Constraints
- Data sources: NCBI E-utilities (esearch + efetch, CORS-open, ~3 req/s) and Europe PMC REST (CORS-open, includes preprints; PUB_TYPE/PUB_YEAR filters, cursorMark paging; no MeSH tree so psych/humans toggles disable there).
- Psych scoping: PubMed MeSH category F via `"behavior and behavior mechanisms"[mh] OR "psychological phenomena"[mh] OR "mental disorders"[mh] OR "behavioral disciplines and activities"[mh]` (verified working).
- Study design: PubMed publication types ([pt]) for filtering; client-side heuristics on abstract text refine the label (e.g., "cross-sectional", "longitudinal cohort", "randomized").
- Extraction is two-tier: regex first pass (N incl. word-numbers, k, p-values, effect sizes incl. R², analysis keywords), plus an optional Claude API pass ("fill gaps" = only where regex is incomplete, "check all" = every abstract) using the user's own API key entered in the UI (stored in localStorage; models: opus 5 / sonnet 5 / haiku 4.5, direct browser fetch with anthropic-dangerous-direct-browser-access). Claude also powers "related terms" synonym suggestions.
- Single-file static HTML app served via Start cut.command (Firefox blocks fetch from file://). No build step, no backend. Users can select studies across searches and export a CSV (title/authors/year/id/doi/design/variables/analysis/findings/N) for meta-analysis work.
- Recent papers (~last few weeks) may lack MeSH indexing and can be missed by the psych filter; the UI must let users toggle the filter off.

## Brand Commitments
- Name: **cut** (user-chosen, lowercase; wordmark "cut.").
- Aesthetic pinned by the user to her own Lykos site (`~/Desktop/Lykos`): white, black Menlo monospace 13px, 1px black boxes, #00f hover, crosshair cursor, lowercase copy.
- No unsolicited content: only features and copy the user asked for. No explainer footers.

## Evidence on Hand
None yet — no logo, no name beyond the working folder ("Search tool"). All result content is real live PubMed data, never fabricated.

## Product Principles
1. The query form speaks psych-methods language, not PubMed syntax.
2. Design quality is visible at a glance — every result wears its study-design label.
3. Zero friction: no login, no key, no install; open the file and search.
4. Honest about mechanism: labels derived heuristically say so; the tool links to the PubMed record as ground truth.
5. Fast scanning beats exhaustive detail — abstracts are for triage, PubMed is for depth.

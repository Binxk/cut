# Design

Visual world: **pinned by the user to her own Lykos site** (`~/Desktop/Lykos`) — white ground, black Menlo monospace, boxes, nothing else. This replaces the earlier forest-plot world.

## Rules (from Lykos source)
- Ground `#fff`, ink `#000`. Links/interactive: black, no underline, hover/selected `#00f`. No other chrome colors.
- Type: `Menlo, monospace` throughout, 13px base, line-height 1.7. Lowercase UI copy ("about", "search", "edit").
- Cursor: `crosshair` everywhere (Lykos signature).
- Boxes: 1px solid `#000`, square corners, white fill. Variables, results summary, and each study get their own box.
- Highlighter `#FFE9A8` retained for matched variable terms in titles/abstracts (functional, pre-dates the restyle).
- No footers, no explainer copy, no decorative anything. Only content the user asked for.

## Layout
- Slim header: `cut.` wordmark (the product name, user-chosen).
- Top search bar rows: terms input · design tick boxes (multi-select, ORed; same checkbox style as scope) · scope (psych/humans toggles grey out on europe pmc, years, sort, source select: pubmed / europe pmc) · claude row (off / fill gaps / check all, model select, api key input persisted in localStorage). Collapses to a one-line summary + `[edit]` after a search runs.
- Two columns: left sidebar (sticky) = variables box (removable boxes; "related terms" button → Claude-suggested synonyms as dashed clickable boxes that append `OR` variants) + results numbers box + selected box (count, export csv, clear). Main column = study boxes, each with a "select" checkbox in its actions row.
- Databox variables render as `.mini` bordered chips, background-coloured by which search variable they belong to (palette `VARCOLORS`; the sidebar variable boxes wear the same colours as the legend; "other"-category chips stay white). Findings render as bold stat + one muted context sentence underneath (context only when the claude pass ran).
- Sources are tick boxes (pubmed / europe pmc / openalex / wos, any combination): the page quota splits between ticked sources. Dedupe: epmc gets `NOT SRC:MED`, openalex gets `has_pmid:false`, wos drops pmid-bearing hits when pubmed is on. WoS needs the user's Clarivate Starter key (input beside the tick box, localStorage `cut_wos_key`) and calls go through the local relay in `cut_server.py` (`/wos`, no CORS upstream); WoS abstracts are hydrated by DOI from OpenAlex. Psych scoping: MeSH on pubmed, concept C15744967 on openalex, unavailable on epmc/wos.
- Info boxes never scroll: 24rem wide, natural height, no height capping.
- Study box: title (bold, term-highlighted), authors/journal, a numeric line (year · N · k · effect sizes found in the abstract · design label), clamped abstract, full abstract / pubmed / doi links.
- Data box (user-specified, right of each study box, 17rem): year / variables / design / analysis / findings / N as label-value lines, "—" when absent. Variables = which search terms appear in that title/abstract; analysis = statistical methods regex-matched from the abstract; findings = p-values + effect sizes.
- Mobile: sidebar stacks above results.

## States
Loading: `searching…` text. Error: named problem + retry. Empty: single lowercase prompt line. No-results: `k = 0` + one suggestion line.

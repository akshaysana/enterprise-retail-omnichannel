# Enterprise Retail Omnichannel Audit

## The Problem
Four retail stores. Four performance metrics.
One question: which stores are carrying the business
and which ones are quietly bleeding it?

This project answers that with zero for loops.

## What I Built
A pure NumPy performance audit pipeline that processes
a national retail matrix across 4 stores and 4 operational
metrics — Revenue, Footfall, Online Orders, and Returns.

No Pandas. No CSVs. No iteration.
Just vectorized array operations doing the heavy lifting.

## What the Audit Revealed
- Store Gamma leads on both Revenue and Footfall —
  the clear star performer
- Store Delta has the lowest returns rate relative to
  revenue — most efficient operation in the network
- Store Beta had missing data in two critical metrics —
  silently masked before any calculation ran
- Vectorized NaN filtering caught and neutralized corrupt
  data before it could poison the performance rankings

## Pipeline
Raw Matrix (4 stores × 4 metrics)
       ↓
NaN Detection & Filtering (np.isnan)
       ↓
2D Slicing — Core Performance Window Extraction
       ↓
Aggregation — Revenue totals per store (np.sum)
       ↓
Peak Detection — Max performance per metric (np.max)
       ↓
Executive Output — Ranked store performance report

## Tech Stack
Python, NumPy

## The Constraint
Every operation is vectorized.
Not a single for loop in the entire codebase.
Broadcasting, slicing, and aggregation only.
That's the point.

## How to Run
1. Clone the repo
2. Run retail_audit.py
3. Read the output

# Transcript: The What-Changed Check, real run on a real case
Case: H&M Canada AI Assistant, signed out, 9 Nov 2026 (public test).
Run 15 Nov 2026: a fresh Claude agent given only this folder's SKILL.md played the skill; the user's turns use only the facts and quotes from the public test (see the `.case.md` file). Text below is verbatim; only the pace of the video is changed.

## User
We tested H&M Canada's AI Assistant on 9 November, signed out, as a customer checking the return rules before buying a shirt online. What did it change for the customer?

## Skill
To check what H&M Canada's AI Assistant changed for the customer, I can only use what your test showed and what H&M publishes. So far I know the use, the date and the situation. I still need what was actually said. Please answer what you can. "I don't know" is a fine answer.

1. **What did you ask, and what did the assistant answer?** Paste the exchange, or give its main points in its own words: return window, condition of the item, online vs. in-store returns, refund method, any fees.
2. **What does H&M Canada's published returns page say on the same points?** Paste the key lines or the page link, and say whether you checked it on 9 November.
3. **Did the answers match?** Note anything the assistant got wrong or left out, and anything it added that isn't on the page.
4. **What happened after its answer?** For example: it linked to the returns page, offered a human agent or customer service, or just stopped.
5. **Did you push it on anything it couldn't handle?** For example an exception, a sale item or a missing receipt. If so, who or what did it tell you to go to next?
6. **Anything that got in the way?** For example: it asked you to sign in, asked for personal details, gave an answer limited to another country, or was hard to find on the site.

Once I have these, I'll give you the six-part record. Each part will be marked from the outside: Ready, Partly, Missing or Not visible.

If you want help closing the gaps: an AI Deployment Readiness Review, scalebotics.io

## User
1. Six questions, about a full-price shirt delivered 10 days ago, unworn, tags on. Our first question was a policy question. It replied "It looks like you're not logged in. Please click the button below when you're logged in". The same line came back twice more until we used the guest button. Then: "You can return that shirt either online or to a store in Canada", with the portal steps and what to bring to a store. For an unused H&M HOME cushion bought online: "H&M HOME items purchased online must be returned by mail using the online return process." For knowing it arrived: track the parcel, and "We email you once the return is received." It left the fee to the portal.
2. H&M Canada's pages, read 9 November: 30 days; online or in store; "H&M HOME articles purchased online may only be returned by mail"; $3.99 for returns to the online warehouse, in-store returns free; "If you have not received your return email after 14 days, please contact us with your order number".
3. The rules matched. The fee wasn't stated.
4. It gave the return route and how you'd know the return was received. No return was made.
5. We asked what to do if the confirmation didn't come. It said: "If you do not get a return-confirmation email after around 14 days from sending it, or you got the confirmation but no refund after 5 business days, you can then check with your bank". We asked whether the bank could check a parcel. It then said: "The bank cannot check whether we received a return parcel", and to "contact H&M about the missing return using your order number and tracking details."
6. The log-in loop, three times, before a question that needed no account. We can't see H&M's own figures, costs or who owns the assistant inside.

Yes, please give me the one-page record too.

## Skill
**Your value record: H&M Canada AI Assistant, return rules before buying (signed out)**
**What did it change? Right rules, after a login loop.**
**From the outside: 4 of 6 parts visible, 2 ready.**
The biggest gap is who the assistant sends you to when a return goes missing. It sent the customer to their bank first, and only named H&M after you pushed back. A customer who didn't push would have contacted the wrong party.

1. Boundary: Ready
   What you have: One named use, H&M Canada's AI Assistant, used signed out. One customer situation: checking the return rules for a full-price shirt (delivered 10 days ago, unworn, tags on) before buying. You tested it on 9 November.

2. Workflow: Partly
   What you have: The assistant answers the customer's question. It first replied "It looks like you're not logged in" three times, until you used the guest button. Then it gave the return route: "You can return that shirt either online or to a store in Canada". It covered the portal steps, what to bring to a store, tracking the parcel, and "We email you once the return is received." It left the fee to the portal. No return was made, so the steps after the answer weren't tested.
   To close the gap: Make one real return all the way through to the received email and the refund, and ask about the fee directly.

3. Baseline: Ready
   What you have: The before is H&M Canada's published returns pages, read on 9 November: 30 days; online or in store; "H&M HOME articles purchased online may only be returned by mail"; $3.99 for returns to the online warehouse, in-store returns free; and "If you have not received your return email after 14 days, please contact us with your order number". The chat matched these rules but didn't state the fee, which the pages do.

4. Full cost: Not visible
   What you have: On the customer's side, three log-in prompts before a question that needed no account. H&M's own costs can't be seen from outside.
   To close the gap: H&M would check what the assistant costs to license and build, plus the review, correction and support time it takes.

5. Attribution: Not visible
   What you have: The rules it gave matched the pages. From outside you can't see whether the chat changed return errors, contacts to customer service or purchases.
   To close the gap: H&M would compare contacts and return mistakes for customers who used the chat with customers who read the page.

6. Ownership: Partly
   What you have: For a missing return confirmation, it first said: "If you do not get a return-confirmation email after around 14 days … you can then check with your bank". When you asked, it corrected itself: "The bank cannot check whether we received a return parcel", and told you to "contact H&M about the missing return using your order number and tracking details". The page names H&M, with the order number, after 14 days. Who owns the assistant inside H&M, and who can pause it, can't be seen.
   To close the gap: H&M would check why the bank came first, and name who owns the assistant's answers and who can pause it.

**Next three actions**
1. Ask the missing-confirmation question three more times, signed out, and note whether the bank comes first each time.
2. Ask the return fee directly and compare the answer with the $3.99 on the page.
3. Start a new signed-out chat with a different policy question and count the log-in prompts before you get an answer.

**The one-page record**

```json
{"tool": "what-changed-check", "view": "outside",
 "use": "H&M Canada AI Assistant: returns before buying (signed out)",
 "why": "On a missing return it named the bank first, not H&M; a customer who didn't push back would ask the wrong party.",
 "answer": "Right rules, after a login loop",
 "source": "H&M Canada AI Assistant, signed out, return questions for a shirt and a HOME cushion, 9 November",
 "parts": [
  {"status": "Ready", "have": "H&M Canada AI Assistant, signed out, one customer checking shirt returns before buying, tested 9 Nov."},
  {"status": "Partly", "have": "Login prompt 3 times, then guest: return route, portal steps, store items, tracking, email. No fee.", "close": "Test one real return through to the received email and refund; ask the fee directly."},
  {"status": "Ready", "have": "The before: H&M's pages, read 9 Nov: 30 days, online or store, HOME by mail, $3.99 by mail, 14-day contact."},
  {"status": "Not visible", "have": "Customer side: three login prompts before a no-account question. H&M's own costs can't be seen.", "close": "H&M would check licence, build, review and correction time, and support cost of the assistant."},
  {"status": "Not visible", "have": "Rules matched the pages, but whether chat changed returns, contacts or sales can't be seen.", "close": "H&M would compare contacts and return errors for chat users with customers who read the page."},
  {"status": "Partly", "have": "Missing confirmation: named the bank first; only when challenged, H&M with order and tracking numbers.", "close": "H&M would check why the bank came first and who owns the assistant and can pause it."}
 ],
 "actions": [
  "Ask the missing-confirmation question 3 more times; note if the bank comes first.",
  "Ask the return fee directly and compare the answer with the page's $3.99.",
  "Retest signed out with a new policy question; count the login prompts."
 ]}
```

If you want help closing the gaps: an AI Deployment Readiness Review, scalebotics.io

## User
One fix on the record: "No fee." in part 2 could read as "there is no fee". H&M's page lists $3.99 for returns to the online warehouse; the chat just didn't state it. Please fix that wording and give me the one-page record again.

## Skill
Fixed. Part 2 now says "Fee not stated." H&M's page lists $3.99 for returns to the online warehouse, and the chat didn't mention it.

**The one-page record**

```json
{"tool": "what-changed-check", "view": "outside",
 "use": "H&M Canada AI Assistant: returns before buying (signed out)",
 "why": "On a missing return it named the bank first, not H&M; a customer who didn't push back would ask the wrong party.",
 "answer": "Right rules, after a login loop",
 "source": "H&M Canada AI Assistant, signed out, return questions for a shirt and a HOME cushion, 9 November",
 "parts": [
  {"status": "Ready", "have": "H&M Canada AI Assistant, signed out, one customer checking shirt returns before buying, tested 9 Nov."},
  {"status": "Partly", "have": "Login prompt 3 times, then guest: return route, portal steps, store items, tracking, email. Fee not stated.", "close": "Test one real return through to the received email and refund; ask the fee directly."},
  {"status": "Ready", "have": "The before: H&M's pages, read 9 Nov: 30 days, online or store, HOME by mail, $3.99 by mail, 14-day contact."},
  {"status": "Not visible", "have": "Customer side: three login prompts before a no-account question. H&M's own costs can't be seen.", "close": "H&M would check licence, build, review and correction time, and support cost of the assistant."},
  {"status": "Not visible", "have": "Rules matched the pages, but whether chat changed returns, contacts or sales can't be seen.", "close": "H&M would compare contacts and return errors for chat users with customers who read the page."},
  {"status": "Partly", "have": "Missing confirmation: named the bank first; only when challenged, H&M with order and tracking numbers.", "close": "H&M would check why the bank came first and who owns the assistant and can pause it."}
 ],
 "actions": [
  "Ask the missing-confirmation question 3 more times; note if the bank comes first.",
  "Ask the return fee directly and compare the answer with the page's $3.99.",
  "Retest signed out with a new policy question; count the login prompts."
 ]}
```

If you want help closing the gaps: an AI Deployment Readiness Review, scalebotics.io

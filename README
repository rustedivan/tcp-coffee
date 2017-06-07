# THE CODE PUB - COFFEE SERVER SERVER
This is an intentionally bad and buggy Python program that helps a coffee shop track orders that are
placed over the web. It starts a web server at localhost:9090. Just run the `coffeebar.py` file and
open `localhost:9090/list` in a web browser to see the flashy interface.

Orders are placed by clicking on the links. The links lead to URLs such as:
- /coffee/order/latte (order one latte)
- /coffee/order/cappucino/3 (order three cappucinos)
These URLs are controlled in `requesthandling.py`.

The available products are listed in a (terrible) database in `products.py`. Every products has a four-digit
ID number which can be used to lookup short names (used in the URLs), long names (for humans to read) and prices.
There are a number of functions that do lookups and conversions of different sorts. This file also contains the
 `place_order` function which is used to actually order products.

Output to the web browser is written as simple HTML from the `weboutput.py` file. This is a very bad way to output
web content. If you're interested in routing/request handling and building web content like this, you will probably
like experimenting with [Tornado](http://tornadoweb.org), specifically `tornado.routing` and `tornado.template`.

Finally, the orders are written into a plain text file on your disk using two functions in `transactionlog.py`.
The orders (mostly buggy!) end up in tcp-coffee-orders.txt in the same directory as the python files so you can find it
easily. If the order file gets long and full of errors, just delete it and it will be re-created.


# Bug reports
The point of TCP COFFEE SERVER SERVER is 1) that it is buggy 2) badly written enough that stepping through it with
a debugger is more convenient. To get you started, here are four bug reports that exercise different concepts in
debugging. Remember: debugging is hard. It is fine to spend a couple of hours and not fixing any of them. The point
is to learn the tools, and most importantly: gaining the confidence to spend time on a single problem. You will punch
through eventually.

- find the problem and how to reproduce it
- diagnose what went wrong
- figure out where and how it went wrong
- fix the bug at the root of the problem
- think about any unwanted side-effects

## Bug 1: Caramelatte Chaos
It seems a lot of people order Caramelattes and never pick them up. To be honest, a lot more
Caramelatte orders come in than we expect...
*How to reproduce:*
1. Start app
2. Order a flat black
3. Order a caramelatte
4. Read the transaction log.
Note that other clients have ordered caramelattes too. Note that they will probably never be picked up and paid for.
*Hint:* Put a breakpoint in the `place_order` function and investigate where calls come from by looking at
the Call Stack. Try a conditional breakpoint to only break when Caramelattes (product ID #5545) are ordered.

## Bug 2: Espresso Errors
Customers complain that they get the wrong order for their espressos. Seems to be something wrong with the
2-shot espresso or something..?
*How to reproduce:*
1. Start app
2. Order a regular espresso
3. Order a 2-shot espresso
4. Read the transaction log
Look at the espresso orders. They are incorrect.
*Hint:* is this a problem with state (data) or logic (code)? How can you investigate that?
Put a breakpoint in the `place_order` function and step through the order to see what's saved to file.
Is there something wrong with the order? Where does the incorrect data _really_ come from?

## Bug 3: Double Trouble
We spent a lot of engineering time on the "2-for-1 discount" feature, but it doesn't work. Nothing happens!
There used to be a problem where a LOT of orders ended up in the file, but now the server just crashes when
baristas use the Double button. There seems to be several problems here so we've sort of given up on it.
We tried to fix it but it made the server crash so that change was backed out from the code.
*How to reproduce:*
1. Start app
2. Use Double button to order a 2-for-1 Mazagran.
3. Note that nothing really happens.
4. Read the transaction log.
Note that the mazagran never enters the log, just those darn extra caramelattes!
*Hint:* There are a lot of problems with this code. Put a breakpoint early in the 2-for-1 order and step through to
where the order is written to the transaction log. Does the program even get there? And if you fix that, why does the
server crash? Is it because your fix is bad, or is it because there are other problems? And once the çrash is fixed,
is the transaction log correct now?

## Bug 4: Mazagran Money
There was a loud argument in the coffee shop after a customer was charged too much for a Mazagran by the barista.
And sometimes we sell them too cheap. This indicates a serious problem with our business logic!
*How to reproduce:*
1. Start app
2. Order a regular black coffe
3. Order a Mazagran
4. Order a Caffeine System Shock
5. Order another Mazagran
6. Read the transaction log
Note that sometimes the Mazagran's price is incorrect (should be 75 kr). Also note that he Mazagran price sometimes changes!
*Hint:* This bug seems to be complex. (And it also depends on whether you have fixed _Bug 1: Caramelatte Chaos_). The
data is clearly incorrect, but where does it come from? Since the price changes if you order different things,
you have a "path dependent" problem.
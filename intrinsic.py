#!/usr/bin/python

val_symbol = ''
val_stock_price = 0.0
val_strike_price = 0.0
val_inc_price_by = 0.0

val_symbol = raw_input("Symbol: ")
val_stock_price = raw_input("Current Stock Price: ")
val_strike_price = raw_input("Strike Price: ")
val_increase_by = raw_input("Increase By: ")

print ("Symbol: %s" % val_symbol.upper())
print ("Stock Price: %8.2f" %  val_stock_price.float())
print ("Strike Price: %8.2f" %  val_strike_price)
print ("Increase By: %8.2f" %  val_increase_by)

# print "Stock Price: ";
# my $stockprice = <STDIN>;
# chomp($stockprice);
# print "Strike Price: ";
# my $strikeprice = <STDIN>;
# chomp ($strikeprice);
# print "Strike Increase: ";
# my $increasestrike = <STDIN>;
# chomp ($increasestrike);
# my $intrinsic = 0.0;
# my$strikecount = 0;
# my $intrinsic = 0;
# printf "Current Price: %6.2f\n", $stockprice;
# foreach $strikecount (0..9) {
# 	$intrinsic = $strikeprice - $stockprice;
# 	# print "Strike Price: ", $strikeprice, "\tIntrinsic Value = ", $intrinsic, "\n";
# 	printf "Strike Price: %6.2f\t", $strikeprice;
# 	printf "Intrinsic Value = %6.2f\n", $intrinsic;
# 	$strikeprice = $strikeprice + $increasestrike;
# }

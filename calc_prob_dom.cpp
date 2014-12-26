#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
double monteAllele(int x, int y, int z) {  
	
	double prob = 10; 
	std::string first_id;
	std::string second_id;
	// sampling 
		
	NumericVector first_draw = runif(1,0,(x+y+z));	
	
	//figure out which to remove 
	if(first_draw[0] < (x)){
		x -= 1;
		first_id = "x";
	} else if(first_draw[0] < (x+y)){
		y -= 1;
		first_id = "y";
	} else {
		z -= 1;
		first_id = "z";
	}
	
	NumericVector second_draw = runif(1,0,(x+y+z));	
	
	if(second_draw[0] < (x)){
		x -= 1;
		second_id = "x";
	} else if(second_draw[0] < (x+y)){
		y -= 1;
		second_id = "y";
	} else {
		z -= 1;
		second_id = "z";
	}
	
	if(first_id == "x" || second_id == "x"){
		prob = 1; 
	}
	if(first_id == "y" && second_id == "y"){
		prob = 0.75; 
	}
	if(first_id == "y" && second_id == "z"){
		prob = 0.5;
	}
	if(first_id == "z" && second_id == "y"){
		prob = 0.5;
	}
	if(first_id == "z" && second_id == "z"){
		prob = 0;
	}
	
	return prob;
	
}

/*** R
monteAllele(2,2,2)
*/
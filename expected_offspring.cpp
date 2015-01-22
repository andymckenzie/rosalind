#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
double expectAllele(int homod_homod, int homod_heter, int homod_homor, int heter_heter, int heter_homor, int homor_homor) {  
	
	double number_offspring = 0; 
	
	number_offspring += homod_homod * 2; 
	number_offspring += homod_heter * 2;
	number_offspring += homod_homor * 2; 
	number_offspring += heter_heter * 1.5; 
	number_offspring += heter_homor * 1; 
	
	return number_offspring;
	
}

/*** R
expectAllele(1, 0, 0, 1, 0, 1)
*/
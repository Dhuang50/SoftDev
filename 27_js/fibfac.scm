;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Team SD :: Suhana Kumar, Danny Huang
;SoftDev PD 5
;W27 - Intro to JS
;2025-01-06
;time: 1

(define fact (lambda (n)
              (if(= n 1)
                 1
                 (* n (fact (- n 1))))))

(define fib (lambda (n)
              (cond
                [(= n 0) 0]
                [(= n 1) 1]
                [else (+ fib(- n 1) fib(- n 2))])))
(fact 1)
(fib 4)
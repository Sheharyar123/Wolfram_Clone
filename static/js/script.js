"use strict";

const dropdownLink = document.querySelector(".menu-trigger");
const dropdownMenu = document.querySelector(".dropdown");
dropdownLink.addEventListener("mouseover", () => {
  dropdownLink.classList.add("show-dropdown");
  dropdownMenu.classList.add("show");
});

dropdownLink.addEventListener("mouseout", () => {
  dropdownLink.classList.remove("show-dropdown");
  dropdownMenu.classList.remove("show");
});

// document.addEventListener("DOMContentLoaded", function () {
//   const selectElement = document.querySelector(".form-select");
//   const options = document.querySelectorAll("option");

//   options.forEach((option) => option.classList.add("custom-option"));

//   // selectElement.addEventListener("focus", () => {
//   //   options.forEach((option) => {
//   //     option.style.backgroundColor = "#fff";
//   //   });
//   // });

//   // selectElement.addEventListener("change", () => {
//   //   options.forEach((option) => {
//   //     option.style.backgroundColor = option.selected ? "#ff" : "#f77700";
//   //   });
//   // });
// });

const hamburger = document.querySelector("#hamburger");
const menuItems = document.querySelector(".nav-links");
hamburger.addEventListener("click", () => {
  menuItems.classList.toggle("show");
});

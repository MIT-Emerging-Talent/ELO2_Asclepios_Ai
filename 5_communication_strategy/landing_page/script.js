// script.js - Enhanced functionality

document.addEventListener('DOMContentLoaded', function() {
    // Model tabs functionality
    const modelTabs = document.querySelectorAll('.model-tab');
    const modelContents = document.querySelectorAll('.model-content');
    
    modelTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const modelId = this.getAttribute('data-model');
            
            // Remove active class from all tabs and contents
            modelTabs.forEach(t => t.classList.remove('active'));
            modelContents.forEach(c => c.classList.remove('active'));
            
            // Add active class to clicked tab
            this.classList.add('active');
            
            // Show corresponding content
            const contentId = modelId + '-model';
            const activeContent = document.getElementById(contentId);
            if (activeContent) {
                activeContent.classList.add('active');
            }
        });
    });
    
    // Add fade-in animations on scroll
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);
    
    // Observe all sections for animation
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
    
    // Form submission handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Here you would typically send the data to a server
            console.log('Form submitted:', data);
            
            // Show success message
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
    }
}); 

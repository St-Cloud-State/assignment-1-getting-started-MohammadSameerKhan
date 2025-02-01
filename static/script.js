document.getElementById("apply-form").onsubmit = async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const zipcode = document.getElementById("zipcode").value;

    const response = await fetch("/apply", {
        method: "POST",
        body: new URLSearchParams({ name, zipcode }),
    });

    const result = await response.json();
    document.getElementById("apply-result").textContent =
        result.application_number ? `Application submitted. Number: ${result.application_number}` : result.error;
};

document.getElementById("status-form").onsubmit = async (e) => {
    e.preventDefault();
    const applicationNumber = document.getElementById("application-number").value;

    const response = await fetch(`/status/${applicationNumber}`);
    const result = await response.json();

    document.getElementById("status-result").textContent =
        result.status ? `Status: ${result.status}` : "Application not found.";
};

document.getElementById("update-form").onsubmit = async (e) => {
    e.preventDefault();
    const applicationNumber = document.getElementById("update-application-number").value;
    const status = document.getElementById("status").value;

    const response = await fetch("/update_status", {
        method: "POST",
        body: new URLSearchParams({ application_number: applicationNumber, status }),
    });

    const result = await response.json();
    document.getElementById("update-result").textContent = result.message || result.error;
};

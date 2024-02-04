// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt


// frappe.ui.form.on('User Registration', {
// 	// refresh: function(frm) {
		
	// after_save: function(frm){
	// 	frm.save();
	// 		frm.call({
	// 		method: 'set_url',
	// 		doc: frm.doc,
		   
	// 	});

	// }
// });
// frappe.ui.form.on('User Registration', {
//     // refresh: function(frm) {
//         frm.page.set_primary_action(__('Save'), function() {
//             frm.save();
//             frm.call({
//                 method: 'set_url',
//                 doc: frm.doc,
//                 callback: function(response) {
//                     // Handle the callback response here if needed
//                 }
//             });
//         });
//     // }
// });

// frappe.ui.form.on('User Registration', {
	
// 	register: function(frm){
// 			frm.call({
// 			method: 'set_url',
// 			doc: frm.doc,
// 		});

// 	}
// });





// frappe.ui.form.on('User Registration', {
// 	// refresh: function(frm) {

// 	// }
	
// 		scan(frm) {
// 		debugger
		 
// 		const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
// 		frm.set_value('current_time', currentTime);
// 		new frappe.ui.Scanner({
// 		dialog: true, // open camera scanner in a dialog
// 		multiple: false, // stop after scanning one value
// 		on_scan(data) {
// 		// frappe.msgprint(data.decodedText);
// 		frm.set_value("qr_code_data", data.decodedText);
// 		}
// 		});
// 		}
// 		});
		
		
		
		// frappe.ui.form.on('QR Code Scan', {
		//   scan_barcode: function(frm) {
		//     new frappe.ui.Scanner({
		//       dialog: true,
		//       multiple: false,
		//       on_scan: function(data) {
		//         frm.set_value('qr_code_data', data.decodedText);
		//       }
		//     });
		//   }
		// });
		
		// frappe.ui.form.on('QR Code Scan', {
		//   scan_barcode: function(frm) {
		//       debugger
		//     let scanner = new Instascan.Scanner({
		//       video: document.getElementById('scanner-container'),
		//       mirror: false,
		//     });
		
		//     scanner.addListener('scan', function(content) {
		//       frm.set_value('qr_code_data', content);
		//       scanner.stop();
		//     });
		
		//     Instascan.Camera.getCameras().then(function(cameras) {
		//       if (cameras.length > 0) {
		//         scanner.start(cameras[0]);
		//       } else {
		//         console.error('No cameras found.');
		//       }
		//     });
		//   }
		// });
		
		// frappe.ui.form.on('QR Code Scan', {
		//   async scan_barcode(frm) {
		// 	const scanner = new Instascan.Scanner({
		// 	  video: document.getElementById('scanner-container'),
		// 	  mirror: false,
		// 	  captureImage: true,
		// 	  refractoryPeriod: 200,
		// 	});
		
		// 	scanner.addListener('scan', async function(content) {
		// 	  frm.set_value('qr_code_data', content);
		// 	  scanner.stop();
		// 	});
		
		// 	try {
		// 	  const cameras = await Instascan.Camera.getCameras();
		// 	  if (cameras.length > 0) {
		// 		const chosenCamera = cameras[0];
		// 		const stream = await navigator.mediaDevices.getUserMedia({
		// 		  video: { deviceId: chosenCamera.id },
		// 		});
		
		// 		const capabilities = chosenCamera.capabilities;
		// 		const resolution = getBestResolution(capabilities);
		
		// 		const constraints = {
		// 		  width: { ideal: resolution.width },
		// 		  height: { ideal: resolution.height },
		// 		};
		
		// 		stream.getTracks().forEach(track => track.stop()); // Stop previous stream if any
		// 		const newStream = await navigator.mediaDevices.getUserMedia({
		// 		  video: { deviceId: chosenCamera.id, ...constraints },
		// 		});
		
		// 		scanner.start(newStream);
		// 	  } else {
		// 		console.error('No cameras found.');
		// 	  }
		// 	} catch (error) {
		// 	  console.error('Error accessing camera:', error);
		// 	}
		//   },
		// });
		
		// function getBestResolution(capabilities) {
		//   // Implement your logic to determine the best resolution based on capabilities
		//   // You can choose the highest resolution, or a resolution suitable for small QR codes
		//   // Example logic: return capabilities.reduce((prev, curr) => prev.width > curr.width ? prev : curr);
		//   // Replace the example logic with your custom logic based on the capabilities object
		//   // You can consider factors like width, height, and frame rate to choose the best resolution.
		//   return capabilities[0]; // Example: Return the first resolution in capabilities
		// }


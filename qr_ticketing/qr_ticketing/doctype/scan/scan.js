// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt



frappe.ui.form.on('scan', {
	
			
	scan(frm) {
		debugger
		
		const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
		frm.set_value('current_time', currentTime);
		new frappe.ui.Scanner({
		dialog: true, // open camera scanner in a dialog
		multiple: false, // stop after scanning one value
		on_scan(data) {
		// frappe.msgprint(data.decodedText);
		frm.set_value("qrcode_data", data.decodedText);

		// const scannedData = data.decodedText;
		frm.refresh_field("qrcode_data")
		}
		});
		}
});




frappe.ui.form.on('scan', {

	qrcode_data: function(frm){
		 
		frm.call({
			method: 'get_data',
			doc: frm.doc,
		});
		frm.refresh_field("user_name")
		frm.clear_table("current_time")
		frm.refresh_field("current_time")

		// frm.save()

	}

});


// button: function(frm){
// 	frm.call({
// 	method: 'get_data',
// 	doc: frm.doc,
// });
// // frm.save();
// // frm.refresh_field("user")
// // frm.refresh_field("event_name")
// },


// frappe.ui.form.on('scan', {
//     refresh: function(frm) {

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





